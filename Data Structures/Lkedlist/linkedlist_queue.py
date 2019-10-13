from datastructures.likedlist.singly_linkedlist import _SinglyLinkedList

class LinkedListQueue(_SinglyLinkedList):
    """FIFO queue implementation using a singly linked list storage."""

    def enqueue(self, e):
        """Add element e to the tail of the queue."""
        self.addTail(e)


    def dequeue(self):
        """
        Remove and return the first element of the queue.
        Raise IndexError if queue is empty
        """
        if self.isEmpty():
            raise IndexError("Queue is empty!.")
        return self.remove()


#TEST
if __name__ == "__main__":
    queue =LinkedListQueue()

    # is em[ty
    print(queue.isEmpty())

    # enqueue
    print("Add element")
    for i in range(3):
        queue.enqueue(i)
        print(i)

    # get len
    print("total element {}".format(len(queue)))

    # get first
    if not queue.isEmpty():
        print("front element : {}".format(queue.first()))

    # dequeue
    print("dequeu")
    while not queue.isEmpty():
        print(queue.dequeue())

    # is_empty
    print(queue.isEmpty())

