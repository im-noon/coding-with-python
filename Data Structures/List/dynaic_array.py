import ctypes

class DynamicArray:
    """A dynamic array class akin to simplified Python's list."""

    def __init__(self):
        """Creat an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return the element at index k."""
        if not 0 <= k < self._n:
            raise IndexError("Invalid index")
        return self._A[k]

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B

    def append(self, obj):
        """Add object to the end of array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

        self._capacity = c

    def insert(self, k, value):
        """Insert value at index k, shifting sequence value rightward"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[k] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value or raise ValueError"""
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError("value not found!")

    def _make_array(self, c):
        """Return a new array with capacity c."""
        return (c * ctypes.py_object)()