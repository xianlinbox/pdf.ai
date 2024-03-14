from langchain.memory import ConversationBufferWindowMemory
from app.chat.models import ChatArgs
from app.chat.memories.sql_message_history import SqlMessageHistory


def build_window_buffer_memory(chat_args: ChatArgs):
    return ConversationBufferWindowMemory(
        chat_memory=SqlMessageHistory(conversation_id=chat_args.conversation_id),
        return_messages=True,
        input_key="chat_history",
        output_key="answer",
        k=2,
    )
