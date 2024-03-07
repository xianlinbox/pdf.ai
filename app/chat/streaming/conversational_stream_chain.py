from langchain.chains import ConversationalRetrievalChain
from app.chat.streaming.streamable_chain import StreamableChain


class CoversationalStreamableChain(StreamableChain, ConversationalRetrievalChain):
    pass
