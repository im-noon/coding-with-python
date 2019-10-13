class CircularQueue:
    """Queue implementation using a single linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class to storing a single linked list node."""

        # streamline memory usage
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            """Initialization node."""
            self._element = element             # refer user's element
            self._next = next                   # refer next node

    def __init__(self):
        """Initialize with empty queue."""
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of element in queue."""
        return self._size

    def isEmpty(self):
        """Return True if queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but not remove) the element at the front of the queue.

        Raise IndexError if queue is empty.
        """
        if self.isEmpty():
            raise IndexError("Queue is empty!.")

        front = self._tail._element
        return front

    def enqueue(self, e):
        """Add and element e to the back of the queue."""
        newest = self._Node(e, None)
        if self.isEmpty():
            newest._next = newest               # initialize circularly
        else:
            newest._next = self._tail._next     # new node point to head
            self._tail._next = newest           # old tail point to new node
        self._tail = newest                     # new node become the tail
        self._size += 1

    def dequeue(self):
        """Remove and return the front element of the queue.

        Raise IndexError if queue is empty.
        """
        if self.isEmpty():
            raise IndexError("Queue is empty!.")
        oldhead = self._tail._next
        if self._size == 1:                     # remove only element
            self._tail = None                   # queue become empty
        else:
            self._tail._next = oldhead._next    # bypass the old head
        self._size -= 1
        return oldhead._element

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next       # old head become the new tail

if __name__ == "__main__":
    dque = CircularQueue()

    print("Add element")
    for i in range(5):
        print("\tadding {}".format(i))
        dque.enqueue(i)

    print("Front element of deque : {}".format(dque.first()))

    print("Rotate queue")
    for i in range(3):
        dque.rotate()

    print("Front element of deque : {}".format(dque.first()))

    print("Deque element")
    while not dque.isEmpty():
        print("\t{}".format(dque.dequeue()))

