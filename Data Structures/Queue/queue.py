class Queue:
    """FIFO queue implementation using a Python list as under laying storage."""
    def __init__(self):
        self._data = []

    def isEmpty(self):
        """Return True if queue is empty."""
        return self._data == []

    def peek(self):
        """Return the element at the front of the queue.
        Raise Empty exception if queue is empty.
        """
        if self.isEmpty():
            raise IndexError("Stack is empty.")
        return self._data[0]

    def enqueue(self, e):
        """Append element e to the queue."""
        self._data.append(e)

    def dequeue(self):
        """Remove and return the element from front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("Stack is empty.")
        return self._data.pop(0)

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(2)
    print(len(q))
    print(q.isEmpty())
    print("-------")
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    print(len(q))
    print("-------")
    print(q.peek())