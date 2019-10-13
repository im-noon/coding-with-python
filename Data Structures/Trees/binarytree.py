#trees/binarytree.py
class BinaryTree(object):
    '''
    Binary tree implementation.
    '''
    class _Node:
        '''
        None public class storing node data.
        '''
        __slot__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._parent =  parent
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def add_left(self, e, node = None):
        newest = self._Node(e)
        if node is None:
            self._root._left = newest
            newest._parent = self._root

        else:
            node._left = newest
            node._left._parent = node
        self._size += 1

    def add_right(self, e, node = None):
        newest = self._Node(e)
        if node is None:
            self._root._right = newest
            newest._parent = self._root
        else:
            node._right = newest
            node._right._parent = node
        self._size += 1

    def add_root(self, e):
        if self._root is not None:
            raise ValueError("Root already exist!")
        self._root = self._Node(e)
        self._size = 1

    def add_node(self, e, node = None):
        if node is None:
            node = self._root

        if self._root == None:
            self.add_root(e)
        else:
            if e <= node._element:
                if node._left is None:
                    self.add_left(e)
                else:
                    self.add_left(e, node._left)
            else:
                if node._right is None:
                    self.add_right(e)
                else:
                    self.add_right(e, node)
