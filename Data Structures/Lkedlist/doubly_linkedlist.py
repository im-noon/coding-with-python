class _DoublyLinkedList:
    """A base class providing double linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for sore a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'  # streamline memory

        def __init__(self, element, prev, next):
            """Initialize node with"""
            self._element = element  # user's element
            self._prev = prev  # reference to previous node
            self._next = next  # reference to next node

    def __init__(self):
        """Create an empty doubly linked list."""
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        """Return the number of element in the list."""
        return self._size

    def isEmpty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add an element between two existing node an return new node."""
        newest = self._Node(e, predecessor, successor)      # link to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete non sentinel node from the list and return it's element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element

        node._prev = node._next = node._element = None   # deprecate node
        return element
