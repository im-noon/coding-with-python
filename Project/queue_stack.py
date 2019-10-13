"""
The aim is to design a queue abstract data type with the help of stacks.
"""


class Queue(object):

    def __init__(self):
        # use one stack for enqueue
        self.enqueue_stack = []
        # use for dequeue
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Stack are empty...")

        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(18)
    q.enqueue(30)

    print(q.dequeue())

    q.enqueue(35)

    print(q.dequeue())