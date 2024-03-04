from langchain.schema import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from langchain.memory import ConversationBufferMemory
from app.chat.models import ChatArgs

from app.web.api import get_messages_by_conversation_id, add_message_to_conversation


class SqlMessageHistory(BaseChatMessageHistory):

    conversation_id: str

    def __init__(self, conversation_id) -> None:
        self.conversation_id = conversation_id
        super().__init__()

    @property
    def message(self):
        return get_messages_by_conversation_id(self.conversation_id)

    def add_message(self, message: BaseMessage) -> None:
        return add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content,
        )

    def clear(self) -> None:
        return super().clear()


def build_memory(chat_args: ChatArgs):
    return ConversationBufferMemory(
        chat_memory=SqlMessageHistory(conversation_id=chat_args.conversation_id),
        return_messages=True,
        input_key="chat_history",
        output_key="answer",
    )
