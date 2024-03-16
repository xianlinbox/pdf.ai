from typing import Any
from langfuse.model import CreateTrace
from app.chat.tracing.lang_fuse import fuse_client


class TracableChain:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        fuse_client.trace(
            CreateTrace(id=self.metadata["conversation_id"], meta_data=self.metadata)
        )
        return super.__call__(*args, **kwds)
