from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Request

from ..shared.utils import get_uptime
from ..drivers.sql.engine import is_ready, get_db

from ..features.chatbot import ChatbotService
from ..features.twilio import TwilioService
from ..features.conversations import ConversationService

app = FastAPI()

@app.get('/health')
def health_check():
    return {"ok": True, "uptime": get_uptime(), "db": is_ready()}

@app.get('/chatbot/config/{id_bot}')
def get_config(id_bot: int, db = Depends(get_db)):
    chatbot = ChatbotService(db)
    return chatbot.get_config(id_bot)

@app.post('/chatbot/webhook/{id_bot}')
async def reply(id_bot: int, request: Request, db = Depends(get_db)):
    
    twilio = TwilioService()
    conversation = ConversationService(db)
    chatbot = ChatbotService(db)
    
    chatbot_config = chatbot.get_config(id_bot)
    context_length = chatbot_config["context_length"]
    base_prompt = chatbot_config["prompt"]

    form_data = await request.form()
    whatsapp_number = twilio.get_sender_wpp_number(form_data)
    user_text_content =  form_data.get("Body")
    
    last_messages = conversation.get_last_messages_by_sender(whatsapp_number, context_length)
    conversation_context = chatbot.build_conversation_context(last_messages, user_text_content, base_prompt)

    chatbot_response = chatbot.get_gpt_response(conversation_context)
    conversation.save_chatbot_interaction(whatsapp_number, user_text_content, chatbot_response)
    twilio.send_wpp_message(whatsapp_number, chatbot_response)

    return # webhook only expects a success response