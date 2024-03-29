"""
Suppose we have a standard linked list.
Construct an in-place (without extra memory) algorithm that
able to find the middle node!

There are two solution:
1. naive solution: we iterate through the list and count how many element
   there are in the list.
   -> The traverse the list again and the node with index total/2 is the
   middle node.

2. using two pointers: we can use two pointers to get the middle node in O(N)
   -> First pointer: traverse the linked list one node at a time
   -> Second pointer: traverse the linked list two node at a time.
   When the faster pointer reaches the end of the linked list, the slow
   pointer is pointing to the middle.
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


    def get_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode

        return slow_pointer

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

    print(linkedlist.get_middle_node().data)