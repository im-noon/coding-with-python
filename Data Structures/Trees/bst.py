class BinarySearchTree(object):
    '''
    The binary search tree implementation.
    '''

    class _Node(object):

        __slots__ = '_element', '_left', '_right'

        def __init__(self, element):
            '''

            :param element:
            '''
            self._element = element
            self._left = None
            self._right = None

    def __init__(self):
        '''

        '''
        self._root = None

    # O(logN) if thee is balance otherwise O(N)
    def _insertNode(self, element, node):
        '''

        :param element:
        :return:
        '''
        if element < node._element:
            if node._left:
                self._insertNode(element, node._left)
            else:
                node._left = self._Node(element)
        else:
            if node._right:
                self._insertNode(element, node._right)
            else:
                node._right = self._Node(element)

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

        return node

    def _getPredeccor(self, node):
        '''

        :param node:
        :return:
        '''
        if node._right:
            return self._getPredeccor(node._right)
        return node


    def insert(self, element):
        '''
        Insert element to the tree
        :param element:
        :return:
        '''
        if not self._root:
            self._root = self._Node(element)
        else:
            self._insertNode(element, self._root)

    def remove(self, element):
        '''

        :param element:
        :return:
        '''
        if self._root:
            self._root = self._removeNode(element, self._root)


    def getMin(self):
        '''

        :return:
        '''
        if self._root:
            return self._getMin(self._root)

    def _getMin(self, node):
        '''

        :param node:
        :return:
        '''
        if node._left:
            return self._getMin(node._left)
        return node._element

    def getMax(self):
        '''

        :return:
        '''
        if self._root:
            return self._getMax(self._root)

    def _getMax(self, node):
        '''

        :param node:
        :return:
        '''
        if node._right:
            return self._getMax(node._right)
        return node._element

    def traverse(self):
        '''

        :return:
        '''
        #if self._root:
        #    self._inorderTraversal(self._root)
        self.inorder()

    def inorder(self):
        '''

        :return:
        '''
        if self._root:
            yield from self._inorderTraversal(self._root)

    def preorder(self):
        '''

        :return:
        '''
        if self._root:
            yield from self._preorderTraversal(self._root)

    def postoder(self):
        '''

        :return:
        '''
        if self._root:
            yield from self._postorderTraversal(self._root)


    def _inorderTraversal(self, node):
        '''
        tree traversal by visit root -> left -> right
        :param node:
        :return:
        '''
        if node._left:
            yield from self._inorderTraversal(node._left)

        yield node._element

        if node._right:
            yield from self._inorderTraversal(node._right)

    def _preorderTraversal(self, node):
        '''
        tree traversal by visit left->root->right
        :param node:
        :return:
        '''

        yield node._element

        if node._left:
            yield from self._preorderTraversal(node._left)

        if node._right:
            yield from self._preorderTraversal(node._right)

    def _postorderTraversal(self, node):
        '''
        tree traversal by visit left -> right -> root
        :param node:
        :return:
        '''

        if node._left:
            yield from self._postorderTraversal(node._left)

        if node._right:
            yield from self._postorderTraversal(node._right)

        yield node._element

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(32)
    bst.insert(10)
    bst.insert(1)
    bst.insert(19)
    bst.insert(16)
    bst.insert(23)
    bst.insert(55)
    bst.insert(79)

    print('-------------------')
    for i in bst.inorder():
        print(i)
    print('+++++++++++++++++++')
    for i in bst.preorder():
        print(i)
    print('*******************')
    for i in bst.postoder():
        print(i)



    print("minimum {}".format(bst.getMin()))

    print("maximum {}".format(bst.getMax()))



