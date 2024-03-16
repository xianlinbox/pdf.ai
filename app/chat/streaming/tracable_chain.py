from typing import Any
from langfuse.model import CreateTrace
from app.chat.tracing.lang_fuse import fuse_client


class TracableChain:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        trace = fuse_client.trace(
            CreateTrace(id=self.meta_data["conversation_id"], meta_data=self.meta_data)
        )
        callbacks = kwds.get("callbacks", [])
        callbacks.append(trace.getNewHandler())
        kwds["callbacks"] = callbacks
        return super.__call__(*args, **kwds)
