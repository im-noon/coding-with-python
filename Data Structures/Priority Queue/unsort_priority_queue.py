#/priority_queue/unsort_priority_queue.py
from datastructures.priority_queue.priority_queue_base import PriorityQueue
from datastructures.likedlist.positional_linkedlist import PositionalList

class UnsortPriorityQueue(PriorityQueue):
    """A min-oriented priority queue implemented with an unsorted list."""

    def __init__(self):
        """Create a new empty priority queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def _findMin(self):
        """Return Position of item with minimum key."""
        if self.isEmpty():
            raise IndexError("Priority queue is empty!")
        small = self._data
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but not remove (key, value) tuple with minimum key."""
        p = self._findMin()
        item = p.element()
        return (item._key, item._value)

    def removeMin(self):
        """Remove and return (key, value) tuple with minimum key."""
        p = self._findMin()
        item = self._data.delete(p)
        return (item._key, item._value)