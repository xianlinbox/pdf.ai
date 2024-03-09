from langchain.chat_models import ChatOpenAI
from app.chat.models import ChatArgs
from functools import partial


def build_llms(chat_args: ChatArgs):
    return ChatOpenAI(streaming=chat_args.streaming)


llm_maps = {
    "gpt-4": partial(build_llms, model_name="gpt-4"),
    "gpt-3.5-turbo": partial(build_llms, model_name="gpt-3.5-turbo"),
}
