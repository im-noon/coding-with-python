"""
Construct an in-place algorithm to reverse a linked list!

There are two solution:
1. naive solution: we consider all the node one by one, then construct
   another linked list in the reverse order.
   >> Problem: it has O(N) memory complexity, so it is not in-place.

2. using two pointers: we can achieve an in-place algorithm that has O(N)
   linear running time complexity.
"""
class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # O(1) !!!
    def insertStart(self, data):

        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self, data):

        if self.head is None:
            return

        self.size = self.size - 1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    # O(1)
    def size1(self):
        return self.size

    # O(N) not good !!!
    def size2(self):

        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode

        return size

    # O(N)
    def insertEnd(self, data):

        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode

    # O(N)
    def reverese(self):
        current_node = self.head
        previouus_node = None
        while current_node:
            next_node = current_node.nextNode
            current_node.nextNode = previouus_node
            previouus_node = current_node
            current_node = next_node
        self.head = previouus_node

if __name__ == "__main__":
    linkedlist = LinkedList()

    linkedlist.insertStart(12)
    linkedlist.insertStart(122)
    linkedlist.insertStart(3)
    linkedlist.insertEnd(31)
    linkedlist.insertEnd(10)
    linkedlist.insertEnd(11)
    linkedlist.insertEnd(26)

    linkedlist.traverseList()

    linkedlist.reverese()
    print("Reverese")
    linkedlist.traverseList()
