"""
The aim is to design a queue abstract data type with the help of stacks.
: use recursion method
"""

class Queue(object):

    def __init__(self):
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    def dequeue(self):

        # base case for recursive method
        if len(self.stack) == 1:
            return self.stack.pop()

        # we keep popping the items until we find the last one
        item = self.stack.pop()

        # we call the method recursively until we find the first item we are
        # insert
        dequeue_item = self.dequeue()

        # after finde the item then we have to insert the items one by one
        self.stack.append(item)

        return dequeue_item

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(18)
    q.enqueue(30)

    print(q.dequeue())

    q.enqueue(35)

    print(q.dequeue())