class Stack:
    """LIFO stack implementation using a Python list as under laying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the number of element in the stack."""
        return len(self._data)

    def isEmpty(self):
        """Return True if stack is empty."""
        return self._data == []

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def peek(self):
        """Return the element at the top of the stack.
        Raise Empty exception if stack is empty.
        """
        if self.isEmpty():
            raise IndexError("Stacke is empty!")
        return self._data[-1]

    def pop(self):
        """Remove and return the element from top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("Stack is empty.")
        return self._data.pop()

# test
if __name__ == "__main__":
    s = Stack()

    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(len(s))
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(len(s))
