import os

import openai

from ..drivers.sql.models import ChatBotConfig, Conversation

class ChatbotService:
    def __init__(self, db):
        self.db = db
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_config(self, id_bot: int) -> dict:
        chatbot_config = self.db.query(ChatBotConfig) \
                .filter(ChatBotConfig.id == id_bot) \
                .first()

        prompt = chatbot_config.prompt if chatbot_config else "Just be friendly and use the persona of a demo NLP chatbot in the context of a Whatsapp Conversation"
        context_length = chatbot_config.context_length if chatbot_config else 3
        
        return {
            "prompt": prompt,
            "context_length": context_length
        }
    
    def build_conversation_context(self, last_messages: Conversation, user_prompt: str, base_prompt: str):
        prompt_context = []
        for message in last_messages:
            prompt_context.append({"role": "user", "content":  message.message})
            prompt_context.append({"role": "assistant", "content":  message.response})
        
        prompt_context.append({"role": "user", "content":  user_prompt})
        prompt_context.append({"role": "system", "content": base_prompt})
        
        return prompt_context
    
    def get_gpt_response(self, context: list):
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=context,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5)
        chatgpt_response = response.choices[0].message.content

        return chatgpt_response
    
