class _SinglyLinkedList:
    """A base class providing single linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked list node."""
        __slot__ = '_element', '_next'      # stramline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of element in the list."""
        return self._size

    def isEmpty(self):
        """Return True if lsit is empty."""
        return self._size == 0

    def addHead(self, e):
        """Insert an element e at the head of the list."""
        self._head = self._Node(e, self._head)
        self._size += 1

    def addTail(self, e):
        """Insert and element e at the tail of  the list."""
        newest = self._Node(e, None)
        if self.isEmpty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def remove(self):
        """Remove an element from the head, and return the head element."""
        if self.isEmpty():
            raise IndexError("Empty element!.")
        front = self._head._element
        self._head = self._head._next
        self._size -= 1
        return front

    def first(self):
        """
        Return (not remove) the first element of the list.
        Raise IndexError if empty.
        """
        if self.isEmpty():
            raise IndexError("Empty element!")
        return self._head._element

    def last(self):
        """
        Return (not remove) the last element of the list.
        Raise IndexError if empty.
        """
        if self.isEmpty():
            raise IndexError("Empty element!")
        return self._tail._element

