from .buffered_memory import build_buffer_memory
from .window_bufferred_memory import build_window_buffer_memory

memories_map = {
    "buffer_memory": build_buffer_memory,
    "window_buffer_memory": build_window_buffer_memory,
}
