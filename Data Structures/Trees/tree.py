
class Tree():
    """Abstract base class representation a tree structure."""


    #  nested Position class
    class Position:
        """Abstract representing of the location of a single element."""

        def element(self):
            """Return the element stored at this position."""
            raise NotImplementedError("must be implemented by subclass!.")

        def __eq__(self, other):
            """Return True if other position represented the same location."""
            raise NotImplementedError("must be implemented by subclass!.")

        def __ne__(self, other):
            """Return True if other does not represented the same location."""
            return not (self == other)

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():
            yield p.element()

    # ------------------------- abstract methods -------------------------------
    def __len__(self):
        """Return the total number of element in this tree."""
        raise NotImplementedError("must be implemented by subclass!.")

    def root(self):
        """Return Position represented the tree's root, None if empty."""
        raise NotImplementedError("must be implemented by subclass!.")

    def parent(self, p):
        """Return Position represented p's parent, None if p is root."""
        raise NotImplementedError("must be implemented by subclass!.")

    def childCount(self, p):
        """Return the number of children at the Position p."""
        raise NotImplementedError("must be implemented by subclass!.")

    def children(self, p):
        """Generate an iteration of Position represented p's children."""
        raise NotImplementedError("must ne implemented by subclass!.")

    # ------------------------- concrete methods -------------------------------
    def isRoot(self, p):
        """Return True is Position p represented the root of this tree."""
        return self.root() == p

    def isLeaf(self, p):
        """Return True id Position p does not have any children."""
        return self.childCount(p) == 0

    def isEmpty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separate Position p from the root."""
        if self.isRoot(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _get_height(self, p):
        """Return the height of the subtree rooted at position"""
        if self.isLeaf(p):
            return 0
        else:
            return 1 + max(self._get_height(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of subtree rooted at Position p."""
        if p is None:
            p = self.root()
        return self._get_height(p)

    def positions(self):
        """Generate an iteration of the tree's position."""
        return self.preorder()  # return entire pre-order iteration

    # ----------------------- Pre order traversal ------------------------------
    def _subtree_preorder(self, p):
        """Generate a pre-order iteration of position in subtree rooted at p.
        Note that if p is a leaf, the loop over the self.children(p) is
        trivial.
        """
        yield p                         # visit p before its subtree
        for c in self.children(p):
            for other in self._subtree_preorder(c): # do pre-order c's subtree
                yield  other            # yielding each to our caller

    def preorder(self):
        """Generate a pre-order iteration of position in the tree."""
        if not self.isEmpty():
            for p in self._subtree_preorder(self.root()):   # start recursion
                yield p


    # ------------------------ Post order traversal ----------------------------
    def _subtree_postorder(self, p):
        """Generate a post-order iteration of positions in subtree rooted at
        p.
        """
        for c in self.children(p):      #for each child
            for other in self._subtree_postorder(c):    # do post-order of c's
                yield  other            # yielding each to our caller
        yield p                         # visit p after it's subtree

    def postorder(self):
        """Generate a post order iteration of positions in the tree."""
        if not self.isEmpty():
            for p in self._subtree_postorder(self.root()):  # start recursion
                yield p
