import os
from functools import partial
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from app.chat.embeddings.openai import embeddings
from app.chat.models import ChatArgs

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV_NAME")
)
vector_store = Pinecone.from_existing_index(
    index_name=os.getenv("PINECONE_INDEX_NAME"), embedding=embeddings
)


def build_retriever(chat_args: ChatArgs, top_k: int = 3):
    search_kwargs = {"filter": {"pdf_id": chat_args.pdf_id}, "k": top_k}
    vector_store.as_retriever(search_kwargs=search_kwargs)


retrievers_map = {
    "2": partial(build_retriever, k=2),
    "3": partial(build_retriever, k=3),
    "5": partial(build_retriever, k=5),
}
