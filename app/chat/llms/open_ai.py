from langchain.chat_models import ChatOpenAI
from app.chat.models import ChatArgs


def build_llms(chat_args: ChatArgs):
    return ChatOpenAI(streaming=chat_args.streaming)
