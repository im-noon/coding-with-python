from datastructures.trees.tree import Tree

class BinaryTree(Tree):
    """Abstract base class represented a binary tree structure."""

    class _Node:
        """Nonpublic class for storing node."""
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element=None, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(Tree.Position):
        """An abstraction representing the location of single element."""
        def __init__(self, container, node):
            """Constructor should not invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same
            location."""
            return type(other) is type(self) and other._node is self._node

    def __init__(self):
        """Initialize empty tree."""
        self._root = None
        self._size = 0

    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type!")
        if p._container is not self:
            raise ValueError("p doen not belong to this container!")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _makePosition(self, node):
        """Return Position instance for a given node (None if no node)."""
        return self.Position(self, node) if node is not None else None

    def _add_root(self, e):
        """Place element e at the root of an empty tree nad return new
        Position.
        Raise ValueError if tree is none empty.
        """
        if self._root is not None:
            raise ValueError("Root already exists.")
        self._size = 1
        self._root = self._Node(e)
        return self._makePosition(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        Raise ValueError if position p is invalid or p already has a left
        child.
        Return the Position of new node.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child already exists.")
        self._size += 1
        self._left = self._Node(e, node)
        return self._makePosition(self._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        Raise ValueError if Position p is invalid or p already has a right
        child.
        Return the Position of new node."""
        node = self._validate(p)
        if node is not None:
            raise ValueError("Right child already exists.")
        self._size += 1
        self._right = self._Node(e,node)
        return self._makePosition(self._right)

    def _replace(self, p , e):
        """Replace the element at position p with e, and return the old
        element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with it's child,
        if any.
        Raise ValueError if Position p is invalid or p has two children.
        Return the element that had been stored at Position p.
        """
        node = self._validate(p)
        if self.childCount(p) == 2:
            raise ValueError("p has two child")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent  # child' grandparent become parent
        if node is self._root:
            self._root = child  # child become root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size += 1
        node._parent = node  # deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external
        Position p.
        """
        node = self._validate(p)
        if not self.isLeaf(p):
            raise ValueError("'Position must be leaft!.")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types mismatch!.")
        self._size += 1
        if not t1.isEmpty():  # attach t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.isEmpty():  # attach t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    # ------------------------- abstract methods -------------------------------
    def __len__(self):
        """Return the total number of element in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._makePosition(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._makePosition(node._parent)

    def children(self, p):
        """Generate an iteration of Position representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def childCount(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    # -------------------------- concrete methods ------------------------------
    def left(self, p):
        """Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        node = self._validate(p)
        return self._makePosition(node._left)

    def right(self, p):
        """Return a Position representing p's right child.
        Return None if p does not have a right child.
        """
        node = self._validate(p)
        return self._makePosition(node._right)

    def sibling(self, p):
        """Return a Position representing p's sibling (None if no sibling)."""
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def positions(self):
        """Generate an iteration of the tree's position."""
        return self.inorder()  # return entire in-order iteration



    # ------------------------ In-order traversal ------------------------------
    def _subtree_inorder(self):
        """Generate an in-order iteration of position in subtree rooted at p."""
        if not self.isEmpty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def inorder(self):
        """Generate an in-order iteration of positions in the tree"""
        if not self.isEmpty():
            for p in self._subtree_inorder(self.root()):    # start recursion
                yield p
