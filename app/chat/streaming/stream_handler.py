from typing import Any
from uuid import UUID
from queue import Queue
from langchain.callbacks.base import BaseCallbackHandler


class StreamCallbackHandler(BaseCallbackHandler):
    queue: Queue

    def __init__(self, queue: Queue) -> None:
        self.queue = queue
        super().__init__()

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        self.queue.put(token)

    def on_llm_end(self, **kwargs: Any) -> Any:
        print("the LLM has finished current stream")
        self.queue.put("--Done--")

    def on_llm_error(self, error: BaseException, **kwargs: Any) -> Any:
        print("the LLM met an error: %s", error)
        self.queue.put("--Done--")
