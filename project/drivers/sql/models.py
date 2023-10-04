from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    message = Column(String)
    response = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class ChatBotConfig(Base):
    __tablename__ = "chatbots"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String)
    context_length = Column(Integer)

    __table_args__ = (
        CheckConstraint('context_length <= 10', name='max_value_constraint'),
        CheckConstraint('context_length >= 0', name='min_value_constraint'),
    )