from langchain.chains import ConversationalRetrievalChain
from app.chat.streaming.streamable_chain import StreamableChain
from .tracable_chain import TracableChain


class CoversationalStreamableChain(
    TracableChain, StreamableChain, ConversationalRetrievalChain
):
    pass
