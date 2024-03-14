from langchain.schema import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from langchain.memory import ConversationBufferMemory
from app.chat.models import ChatArgs
from app.chat.memories.sql_message_history import SqlMessageHistory
from app.web.api import get_messages_by_conversation_id, add_message_to_conversation


def build_buffer_memory(chat_args: ChatArgs):
    return ConversationBufferMemory(
        chat_memory=SqlMessageHistory(conversation_id=chat_args.conversation_id),
        return_messages=True,
        input_key="chat_history",
        output_key="answer",
    )
