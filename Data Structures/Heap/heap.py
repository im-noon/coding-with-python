#./heap/heap.py

class Heap():
    '''
    Tree like representation of heap data structure.
    '''
    def __init__(self, capacity):
        '''
        Initialize with maximum size.
        :param capacity: maximum size.
        '''
        self._capacity = capacity
        self._heap = [0] * capacity
        self._heapSize = 0

    def _isFUll(self):
        '''
        Check the available capacity of heap.
        :return: True if heap is full.
        '''
        return self._heapSize == self._capacity

    def _swap(self, index1, index2):
        '''
        Swap two items with index1, index2 in the heap array
        :param index1: child index
        :param index2: parent index
        :return:
        '''
        self._heap[index2], self._heap[index1] = self._heap[index1], \
                                                 self._heap[index2]

    # O(Log N)
    def _fixUp(self, index):
        '''
        Consider the last item and check weather swaps are needed or not
        :param index:
        :return:
        '''
        parent_index = (index - 1) // 2

        # while the index > 0 means until we consider all the items "above"
        # the on we inserted we have to swap the node with the parent if the
        # heap property is violated, it is a MAX HEAP: largest are in the root
        if index > 0 and self._heap[index] > self._heap[parent_index]:
            self._swap(index, parent_index)
            self._fixUp(parent_index)

    # O(log N)
    def _fixDown(self, index):
        '''
        Heap violated check for al the item below the given index
        :param index:
        :return:
        '''
        parentIndex = index
        leftIndex = 2 * index + 1
        rightIndex = 2 * index + 2

        # if the left child is greater that the parent : largest is the left.
        if leftIndex < self._heapSize and self._heap[leftIndex] > self._heap[
            index]:
            parentIndex = leftIndex

        # if the right child is grater than the left child: largest is the
        # right.
        if rightIndex < self._heapSize and self._heap[rightIndex] > \
                self._heap[parentIndex]:
            parentIndex = rightIndex

        # do not want to swap items with themselves
        if index != parentIndex:
            self._swap(index, parentIndex)
            self._fixDown(parentIndex)



    # O(1)
    def peek(self):
        '''
        Return the root node, because it is a max heap
        :return:
        '''
        return self._heap[0]

    # O(log N)
    def poll(self):
        '''
        Return the maximum and remove the maximum item.
        :return:
        '''
        max = self.peek()

        self._swap(0, self._heapSize - 1)
        self._heapSize -= 1
        self._fixDown(0)

        return max

    # O(log N)
    def push(self, item):
        '''
        Insert an item to heap.
        :param item:
        :return:
        '''
        if self._isFUll():
            return

        self._heap[self._heapSize] = item
        self._heapSize += 1;

        # heap violated check
        self._fixUp(self._heapSize - 1)

    # O( NlogN)
    def sort(self):
        '''
        Sorting the heap items
        :return:
        '''
        size = self._heapSize
        for i in range(0, size):
            temp = self.poll()
            print(temp)

if __name__ == "__main__":
    heap = Heap(10)
    heap.push(10)
    heap.push(-20)
    heap.push(0)
    heap.push(2)
    heap.push(4)
    heap.push(5)
    heap.push(6)
    heap.push(7)
    heap.push(20)
    heap.push(15)

    heap.sort()