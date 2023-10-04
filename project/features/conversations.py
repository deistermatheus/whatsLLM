from ..drivers.sql.models import Conversation
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError

class ConversationService:
    def __init__(self, db):
        self.db = db

    def get_last_messages_by_sender(self, sender: str, limit: int):
        messages = self.db.query(Conversation) \
            .filter(Conversation.sender == sender) \
            .order_by(desc(Conversation.created_at)) \
            .limit(limit)

        return messages
    
    def save_chatbot_interaction(self, sender: str, message: str, response: str):
        try:
            conversation = Conversation(
                sender=sender,
                message=message,
                response=response
                )
            self.db.add(conversation)
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()
          



