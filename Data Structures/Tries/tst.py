class TST():
    '''
    The ternary search tree implementation.
    '''
    class _Node():
        '''
        Lightweight, nonpublic class for store a node data.
        '''
        __slots__ = '_char', '_left', '_right', '_middle', '_data'
        def __init__(self, char):
            self._char = char
            self._left = None
            self._right = None
            self._middle = None
            self._data = 0

    def __init__(self):
        self._rootNode = None

    def _putItem(self, node, key, value, index):
        '''

        :param key:
        :param value:
        :param index:
        :return:
        '''
        char = key[index]

        if node == None:
            node = self._Node(char)

        if char < node._char:
            node._left = self._putItem(node._left, key, value, index)
        elif char > node._char:
            node._right = self._putItem(node._right, key, value, index)
        elif index < len(key) - 1:
            node._middle = self._putItem(node._middle, key, value, index + 1)
        else:
            node._data = value

        return node

    def _getItem(self, node, key, index):
        '''

        :param node:
        :param key:
        :param index:
        :return:
        '''
        if node == None:
            return None

        char = key[index]
        if char < node._char:
            return self._getItem(node._left, key, index)
        elif char > node._char:
            return self._getItem(node._right, key, index)
        elif index < len(key) - 1:
            return self._getItem(node._middle, key, index + 1)
        else:
            return node

    def put(self, key, value):
        '''
        Insert new element to the tree
        :param key:
        :param data:
        :return:
        '''
        self._rootNode = self._putItem(self._rootNode, key, value, 0)

    def get(self, key):
        '''
        Get element with specify key
        :param key: key pair
        :return:
        '''
        node = self._getItem(self._rootNode, key, 0)
        if node == None:
            return -1
        return node._data


if __name__ == "__main__":
    tst = TST()
    tst.put("apple", 100)
    tst.put("orange", 200)

    print(tst.get("apple"))