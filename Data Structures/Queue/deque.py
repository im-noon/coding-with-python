# datastructures/deque.py

class Deque:
    '''
    Deque abstract data type
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        '''
        Add the item from last
        :param item: the item to add
        :return: None
        '''
        self.items.append(item)

    def addRear(self, item):
        '''
        Add the item from front
        :param item: the item to add
        :return: None
        '''
        self.items.insert(0, item)

    def removeFront(self):
        '''
        Remove the last element
        :return: the front item
        '''
        return self.items.pop()

    def removeRear(self):
        '''
        Remove the first element
        :return: the first element
        '''
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    d = Deque()
    print(d.isEmpty())
    d.addRear(4)
    d.addRear('dog')
    d.addFront('cat')
    d.addFront(True)
    print(len(d))
    print(d.isEmpty())
    d.addRear(8.4)
    print(d.removeRear())
    print(d.removeFront())
    print(len(d))