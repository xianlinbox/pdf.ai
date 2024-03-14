import os
from langfuse.client import Langfuse

fuse_client = Langfuse(
    os.getenv("LANGFUSE_PUBLIC_KEY"),
    os.getenv("LANGFUSE_SECRET_KEY"),
    host="hhtps://prod-langfuse.fly.dev",
)
