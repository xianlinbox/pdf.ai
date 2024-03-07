from typing import Any, Dict, Iterator
from langchain_core.runnables.config import RunnableConfig


class StreamableChain:

    def stream(
        self,
        input: Dict[str, Any],
        config: RunnableConfig | None = None,
        **kwargs: Any | None
    ) -> Iterator[Dict[str, Any]]:
        self(input)
        return super().stream(input, config, **kwargs)
