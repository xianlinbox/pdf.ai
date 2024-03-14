from typing import Any


class TracableChain:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super.__call__(*args, **kwds)
