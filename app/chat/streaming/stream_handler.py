from typing import Any, Dict, List
from uuid import UUID
from queue import Queue
from  import Set
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.messages import BaseMessage

END_SIGNAL = "--Done--"


class StreamCallbackHandler(BaseCallbackHandler):

    def __init__(self, queue: Queue) -> None:
        self.queue = Queue()
        self.streaming_run_ids = set()

    def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        run_id: UUID,
    ) -> Any:
        if serialized["kwargs"]["Streaming"] == True:
            self.streaming_run_ids.add(run_id)

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        self.queue.put(token)

    def on_llm_end(self, run_id, **kwargs: Any) -> Any:
        print("the LLM has finished current stream")
        if run_id in self.streaming_run_ids:
            self.queue.put(END_SIGNAL)
            self.streaming_run_ids.remove(run_id)

    def on_llm_error(self, run_id, error: BaseException, **kwargs: Any) -> Any:
        print("the LLM met an error: %s", error)
        if run_id in self.streaming_run_ids:
            self.queue.put(END_SIGNAL)
            self.streaming_run_ids.remove(run_id)
