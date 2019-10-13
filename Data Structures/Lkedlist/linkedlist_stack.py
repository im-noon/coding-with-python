from datastructures.likedlist.singly_linkedlist import _SinglyLinkedList

class LinkedListStack(_SinglyLinkedList):
    """LIFO Stack implementation using linked list for storage."""

    def push(self, e):
        """Add element e to the top of the stack"""
        self.addHead(e)

    def pop(self):
        """Remove and return the top element from the stack.
        Raise IndexError if stack is empty.
        """
        if self.isEmpty():
            raise IndexError("Stack is empty!.")
        return self.remove()

    def top(self):
        """
        Return but not remove the top element op the stack.
        Raise IndexError if stack is empty.
        """
        if self.isEmpty():
            raise IndexError("Stack is empty!.")
        return self.first()


if __name__ == "__main__":
    stack = LinkedListStack()

    # is empty?
    print(stack.isEmpty())

    # add element

    print("Add element...")
    for i in range(3):
        print(i)
        stack.push(i)
    # get top

    if not stack.isEmpty():
        print("top element {}".format(stack.top()))

    # pop all element
    print("Pop element...")
    while not stack.isEmpty():
        e = stack.pop()
        print(e)

    # is empty?
    print(stack.isEmpty())