class UnorderList:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        """Create empty list"""
        self._head = self._Node(None, None)
        self._size = 0

    def __len__(self):
        """Return the number of element in the list."""
        return self._size

    def __iter__(self):
        cursor = self._head
        while cursor._next is not None:
            yield cursor._element
            cursor = cursor._next


    def isEmpty(self):
        """Return True if list is empty"""
        return self._size == 0

    def add(self, element):
        """
        Adds a new element to the list.
        :param element: new element to added
        :return: None
        """
        self._head = self._Node(element, self._head)
        self._size += 1

    def append(self, element):
        """
        Adds a new element to the end of the list making it the last element in the collection
        :param element: new element to added
        :return: None
        """
        self.add(element)


    def search(self, element):
        """
        Searches for the item in the list. It needs the item and returns a
        boolean value.
        :param element:
        :return:
        """
        for item in self:
            if element == item:
                return True
        return False

    def index(self, element):
        """
        Returns the position of element in the list.
        Assume the element is in the list.
        :param element: the target item
        :return: the position of the target
        """
        index = 0
        for item in self:
            if element == item:
                return index
            index += 1
        return None

    def remove(self, element):
        """
        Removes the element from the list.
        Assume the element is present in the list.
        :param element: target element to remove
        :return: None
        """
        prev = None
        cursor = self._head
        next = cursor._next
        while cursor is not None:
            if element == cursor._element:
                break
            prev = cursor
            cursor = cursor._next
            next = cursor._next

        if next is not None:
            prev._next = next
            self._size -= 1

    def pop(self):
        """
        Removes and returns the last element in the list
        :return: the last element in the list
        """
        if self._size > 0:
            head_element = self._head._element
            self._head = self._head._next
            self._size -= 1
            return head_element
        else:
            raise IndexError("List is empty")

    def pop(self, index=None):
        """
        Removes and returns the element at index.
        Assume the item is in the list.
        :param index: the position to remove
        :return: the element at  index
        """
        if index is None:
            if self._size > 0:
                head_element = self._head._element
                self._head = self._head._next
                self._size -= 1
                return head_element
            else:
                raise IndexError("List is empty")

        elif index <= self._size:
            node_index = 0
            prev = None
            cursor = self._head
            next = cursor._next
            while cursor is not None:
                if index == node_index:
                    break
                prev = cursor
                cursor = cursor._next
                next = cursor._next
                node_index += 1

            if next is not None:
                prev._next = next
                self._size -= 1
            element = cursor._element
            return element
        else:
            raise IndexError("Index out of bound")


if __name__ == "__main__":

    mylist = UnorderList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print("current len : {}".format(len(mylist)))
    print("iter all element")
    for item in mylist:
        print(item)

    print("\nsearch:...")
    print("99 is found : {}".format(mylist.search(26)))
    print("99 is found : {}".format(mylist.search(99)))
    print(("\nindex:..."))
    print("index of 26 : {}".format(mylist.index(26)))
    print("index of 77 : {}".format(mylist.index(77)))

    print("\nremove 93:")
    mylist.remove(93)
    print("\ncurrent len : {}".format(len(mylist)))
    print("iter all element")
    for item in mylist:
        print(item)

    print("\npop()    : {}".format(mylist.pop()))
    print("iter all element")
    for item in mylist:
        print(item)
    print("\npop(2)   : {}".format(mylist.pop(2)))
    print("iter all element")
    for item in mylist:
        print(item)
