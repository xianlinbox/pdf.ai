from typing import Any, Dict, Iterator
from app.chat.streaming.stream_handler import StreamCallbackHandler
from queue import Queue


class StreamableChain:

    def stream(
        self, input: Dict[str, Any], **kwargs: Any | None
    ) -> Iterator[Dict[str, Any]]:
        token_queue = Queue()
        stream_callback = StreamCallbackHandler(queue=token_queue)

        self(input, callback=[stream_callback])

        while True:
            yield token_queue.get()
