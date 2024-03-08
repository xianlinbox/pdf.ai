from typing import Any, Dict, Iterator
from queue import Queue
from threading import Thread
from app.chat.streaming.stream_handler import StreamCallbackHandler
from app.chat.streaming.stream_handler import END_SIGNAL


class StreamableChain:

    def stream(
        self, input: Dict[str, Any], **kwargs: Any | None
    ) -> Iterator[Dict[str, Any]]:
        token_queue = Queue()
        stream_callback = StreamCallbackHandler(queue=token_queue)

        def task():
            self(input, callback=[stream_callback])

        Thread(target=task).start()

        while True:
            token = token_queue.get()
            if token == END_SIGNAL:
                break
            yield token_queue.get()
