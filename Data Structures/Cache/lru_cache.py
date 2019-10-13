# least recently used cache


class Node(object):

    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dictionary = {}
        self.linked_list = DoublyLinkedList()

    def put(self, id, data):

        # update the node if it already exists
        if id in self.dictionary:
            node = self.dictionary[id]
            node.data = data

            # move the node to the head if linked list
            self.update(node)
            return

        # if the data not present in the cache so insert
        node = Node(id, data)

        # add new item the the hard if cache is not full
        if self.size < self.capacity:
            self.size += 1
            self.add(node)
        else: # remove the tail item
            self.remove_tail()
            self.add(node)

    def add(self, node):

        # the node will be the new head
        node.next = self.linked_list.head
        node.prev = None

        # update the previous head to the new head
        if self.linked_list.head:
            self.linked_list.head.prev = node

        # update the head
        self.linked_list.head = node

        # if there is 1 node in the linked list, the tail is point to the
        # same as the head
        if not self.linked_list.tail:
            self.linked_list.tail = node

        # update the dictionary with the node
        self.dictionary[node.id] = node

    def remove_tail(self):
        """
        Remove the least frequently used
        :return: Node
        """

        # get the tail node
        last_node = self.dictionary[self.linked_list.tail.id]
        self.linked_list.tail = last_node.prev

        # reset the tail next node to None
        if self.linked_list.tail:
            self.linked_list.tail.next = None

        # remove the tail node
        last_node = None

    def get(self, id):
        """
        Get the item with id and move it to the head with shift the other
        item to right accordingly.
        :param id: node id
        :return: data with id
        """
        node = None
        if id in self.dictionary:
            node = self.dictionary[id]
            self.update(node)

        return node

    def update(self, node):
        """
        Update the given node to the head
        :param node: most frequently used item
        :return: None
        """

        # get the previous and next node
        prev_node = node.prev
        next_node = node.next

        # if node is in the middle
        if prev_node:
            prev_node.next = next_node
        else: # we know that this node is the head
            self.linked_list.head = next_node

        # if not the last node
        if next_node:
            next_node.prev = prev_node
        else: # if it the last node
            self.linked_list.tail = prev_node

        # move the node to the head
        self.add(node)


    def show(self):
        node = self.linked_list.head
        while node:
            print("{} ->".format(node.data))
            node = node.next

if __name__ == "__main__":

    cache = LRUCache(5)

    cache.put(0, 'A')
    cache.put(1, 'B')
    cache.put(2, 'C')
    cache.put(3, 'D')
    cache.put(4, 'E')
    cache.put(5, 'F')
    cache.put(6, 'G')

    cache.show()

    print("Getting node: ", cache.get(6).data)
    cache.show()
    print()

    print("Getting node: ", cache.get(3).data)
    cache.show()
    print()

    print("Getting node: ", cache.get(4).data)
    cache.show()

