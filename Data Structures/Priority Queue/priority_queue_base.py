# /priority_queue/priority_queue_base.py

class PriorityQueue:
    """Abstract base class representing priority queue item."""

    class _Item:
        """Composite class storing priority queue item."""
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            """Compare items base on key."""
            return self._key < other._key

    def isEmpty(self):
        """Return True if the priority queue is empty."""
        return len(self) == 0
    