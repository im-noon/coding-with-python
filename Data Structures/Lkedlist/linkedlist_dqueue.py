from datastructures.likedlist.doubly_linkedlist import _DoublyLinkedList


class LinkedDeque(_DoublyLinkedList):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but not remove) the element at the front of the deque.
        Raise IndexError if deque is empty.
        """
        if self.isEmpty():
            raise IndexError("Deque is empty!.")
        return self._head._next._element

    def last(self):
        """Return (but not remove) the element at the back of the deque.
        Raise IndexError if deque is empty.
        """
        if self.isEmpty():
            raise IndexError("Deque is empty!.")
        return self._tail._prev._element

    def insert_first(self, e):
        """Add an element e to the front of the deque."""
        self._insert_between(e, self._head, self._head._next)   # after head

    def insert_last(self, e):
        """Add an element e to the back of the deque."""
        self._insert_between(e, self._tail._prev, self._tail)   # before tail

    def delete_first(self):
        """Remove and return the element from the front of the deque."""
        if self.isEmpty():
            raise IndexError("Deque is empty!.")
        return self._delete_node(self._head._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque."""
        if self.isEmpty():
            raise IndexError("Deque is empty.")
        return self._delete_node(self._tail._prev)


if __name__ == "__main__":
    dque = LinkedDeque()

    print("Add element to front")
    for i in range(5):
        print("\tadding {}".format(i))
        dque.insert_first(i)

    print("Front element of deque : {}".format(dque.first()))
    print("Back element of deque : {}".format(dque.last()))

    print("Add element to Last")
    for i in range(6, 10):
        print("\tadding {}".format(i))
        dque.insert_last(i)

    print("Front element of deque : {}".format(dque.first()))
    print("Back element of deque : {}".format(dque.last()))
