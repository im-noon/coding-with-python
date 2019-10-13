#/priority_queue/sorted_priority_queue.py

from datastructures.priority_queue.priority_queue_base import PriorityQueue
from datastructures.likedlist.positional_linkedlist import PositionalList

class SortedPriorityQueue(PriorityQueue):
    """A min-oriented priority queue implemented with sorted list."""

    def __init__(self):
        """Create a new empty priority queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (key, value) tuple with minimum key."""
        if self.isEmpty():
            raise IndexError("Priority queue is  empty.")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def removeMin(self):
        """Remove and return (key, value) tuple with minimum key."""
        if self.isEmpty():
            raise IndexError("Priority queue is empty.")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
