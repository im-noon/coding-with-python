class AVLTree(object):
    '''
    (AVL)Balanced tree implementation.
    '''
    class _Node(object):
        __slots__ = '_element', '_left', '_right', '_height'

        def __init__(self, element):
            self._element = element
            self._left = None
            self._right = None
            self._height = 0;

    def __init__(self):
        self._root = None

    def _getHeight(self, node):
        '''

        :param node:
        :return:
        '''
        if not node:
            return -1

        return node._height

    def _isBalance(self, node):
        '''
        Validate node is balanced or unbalanced.
        If height > 1 that mean left heavy tree then proceed right rotation.
        If height < -1 that mean right heavy tree then proceed left rotation.
        :param node: node
        :return: height of the tree
        '''
        if not node:
            return 0

        return self._getHeight(node._left) - self._getHeight(node._right)

    def _rotateRight(self, node):
        '''
        Rotation to right
        :param node: rotation node
        :return:
        '''
        print("-> rotating to the right on node:{}".format(node._element))
        tempLeft = node._left
        tempRight = tempLeft._right

        tempLeft._right = node
        node._left = tempRight

        node._height = max(self._getHeight(node._left), self._getHeight(
            node._right)) + 1
        tempLeft._height = max(self._getHeight(tempLeft._left),
                               self._getHeight(tempLeft._right)) + 1
        return tempLeft

    def _rotatLeft(self, node):
        '''

        :param node: rotation node
        :return:
        '''
        print("-> rotating to the left on node :{}".format(node._element))
        tempRight = node._right
        tempLeft = tempRight._left

        tempRight._left = node
        node._right = tempLeft

        node._height = max(self._getHeight(node._left), self._getHeight(
            node._right)) + 1
        tempRight._height = max(self._getHeight(tempRight._left),
                                self._getHeight(tempRight._right)) + 1

        return tempRight

    def _violationNode(self, element, node):
        '''

        :param element:
        :param node:
        :return:
        '''
        balance = self._isBalance(node)

        # case I left left heavy
        if balance > 1 and element < node._left._element:
            print('Left left heavy situation...')
            return self._rotateRight(node)

        # case II right right heavy
        if balance < -1 and element > node._right._element:
            print('Right right heavy situation...')
            return self._rotatLeft(node)

        # case III left right heavy
        if balance > 0 and element > node._left._element:
            print('Left right heavy situation')
            node._left = self._rotatLeft(node._left)
            return self._rotateRight(node)

        # case IV right left rotation
        if balance < -1 and element < node._right._element:
            print('Right left heavy situation')
            node._right = self._rotateRight(node._right)
            return self._rotatLeft(node)

        return node

    def _insertNode(self, element, node):
        '''

        :param element: data to insert
        :param node: node to insert
        :return:
        '''
        if not node:
            return self._Node(element)

        if element < node._element:
            node._left = self._insertNode(element, node._left)
        else:
            node._right = self._insertNode(element, node._right)

        node._height = max(self._getHeight(node._left), self._getHeight(
            node._right)) + 1

        return self._violationNode(element, node)

    def _removeNode(self, element, node):
        '''
        Remove node that contain element
        :param element:
        :param node:
        :return:
        '''
        if not node:
            return node

        if element < node._element:
            node._left = self._removeNode(element, node._left)
        elif element > node._element:
            node._right = self._removeNode(element, node._right)
        else:
            if not node._right and not node._left:
                print("Removing a leaf node...")
                return None

            if not node._left:
                print("Removing a node with left child...")
                tempNode = node._right
                del node
                return tempNode
            elif not node._right:
                print("Removing a node with left child...")
                tempNode = node._left
                del node
                return tempNode

            print("removing node with two child...")
            tempNode = self._getPredeccor(node._left)
            node._element = tempNode._element
            node._left = self._removeNode(tempNode._element, node._left)

        # the the tree had only single node
        if not node:
            return node

        # proceed rotating to keep balance
        node._height = max(self._getHeight(node._left), self._getHeight(
            node._right)) + 1

        balance = self._isBalance(node)

        # doubly left heavy
        if balance > 1 and self._isBalance(node._left) >= 0:
            return self._rotateRight(node)


        # left right heavy
        if balance > 1 and self._isBalance(node._left) < 0:
            node._left = self._rotatLeft(node._left)
            return self._rotateRight(node)

        # right right
        if balance < -1 and self._isBalance(node._right) <= 0:
            return self._rotatLeft(node)

        # right left
        if balance < -1 and self._isBalance(node._right) > 0:
            node._right = self._rotateRight(node._right)
            return self._rotatLeft(node)

        return node

    def _getPredeccor(self, node):
        '''

        :param node:
        :return:
        '''
        if node._right:
            return self._getPredeccor(node._right)
        return node

    def _inorderTraversal(self, node):
        '''

        :param node:
        :return:
        '''
        if node._left:
            yield from self._inorderTraversal(node._left)

        yield node._element

        if node._right:
            yield from self._inorderTraversal(node._right)

    def traverse(self):
        if self._root:
            yield from self._inorderTraversal(self._root)

    def insert(self, element):
        '''

        :param element: data to insert
        :return:
        '''
        self._root = self._insertNode(element, self._root)

    def remove(self, element):
        '''

        :param element:
        :return:
        '''
        if self._root:
            self._root = self._removeNode(element, self._root)

if __name__ == "__main__":
    avl = AVLTree()
    avl.insert(10)
    avl.insert(20)
    avl.insert(5)
    avl.insert(6)
    avl.insert(15)

    print('-------------------')
    for e in avl.traverse():
        print('-> {}'.format(e))

    avl.remove(15)
    avl.remove(20)
    print('+++++++++++++++++++')
    for e in avl.traverse():
        print('-> {}'.format(e))
