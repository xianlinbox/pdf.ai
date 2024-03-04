from langchain.chains import ConversationalRetrievalChain
from app.chat.models import ChatArgs
from app.chat.vector_store.pinecone import build_retriever
from app.chat.memories.sql_message_memory import build_memory
from app.chat.llms.open_ai import build_llms


def build_chat(chat_args: ChatArgs):
    retriever = build_retriever(chat_args=chat_args)
    memory = build_memory(chat_args=chat_args)
    llm = build_llms(chat_args=chat_args)
    return ConversationalRetrievalChain.from_llm(
        memory=memory, retriever=retriever, llm=llm
    )
