from datastructures.likedlist.doubly_linkedlist import _DoublyLinkedList


class PositionalList(_DoublyLinkedList):
    """A sequential container of element allowing positional access."""

    # nested Position class
    class Position:
        """An abstract representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element at this position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same
            location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    # ----------------------- utility method
    def _validate(self, p):
        """Return position's node or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type!.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._next is None:
            raise ValueError('p is no longer valid!.')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (None if sentinel)."""
        if node is self._head or node is self._tail:
            return None                             # boundary violation
        else:
            return self.Position(self, node)        # legitimate position

    # ----------------------- accessor
    def first(self):
        """Return the first Position in the list (None if list is empty)."""
        return self._make_position(self._head._next)

    def last(self):
        """Return the last Position in the list (None of list is empty)."""
        return self._make_position(self._tail._prev)

    def before(self, p):
        """Return the Position just before Position p (None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration if the element of the lsit."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ----------------------- accessor
    # override inherited version to return Position, rather that Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._head, self._head._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._tail._prev, self._tail)

    def add_before(self, p, e):
        """Insert element e into the list before Position p and return new
        Position."""
        origin = self._validate(p)
        return self._insert_between(e, origin._prev, origin)

    def add_after(self, p, e):
        """Insert element e into the list after Position p and return new
        Position."""
        origin = self._validate(p)
        return self._insert_between(e, origin, origin._next)

    def delete(self, p):
        """Remove and return tge element at Position p."""
        origin = self._validate(p)
        return self._delete_node(origin)

    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formerly at Position p.
        """
        origin = self._validate(p)
        old_element = origin._element           # temporarily store old element
        origin._element = e                     # replace with new element
        return old_element
