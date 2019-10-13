"""
x = x&(-x)
x = x+(x&(-x))
"""

class FenwickTree(object):
    """Fenwick tree of binary indexed tree."""

    def __init__(self, nums):
        """
        Initialize the value of fenwick tree.
        :param nums: the original array of numbers
        """
        self.nums = nums
        self.fenwick_tree = [0 for _ in range(len(nums) + 1)]
        self.construct()

    def next(self, index):
        """
        Compute the next index of left item.
        O(1) running time complexity.
        :param index: the index of the item
        :return: next index
        """
        return index + (index&-index)

    def parent(self, index):
        """
        Compute the index of the item on the right.
        O(1) running time complexity.
        :param index: the index of the item
        :return: parent index
        """
        return index - (index&-index)

    def construct(self):
        """
        Construction the three
        O(NlogN) running time complexity.
        """

        for index in range(1, len(self.nums) + 1):
            self.update(index, self.nums[index - 1])

    def update(self, index, num):
        """
        Update the existing item in the tree with index and value accordingly
        O(logN) running time complexity.
        :param index: index update item
        :param num: value of update index
        :return: None
        """
        while index < len(self.nums) + 1:
            self.fenwick_tree[index] += num

            # index of the next item should update to
            index = self.next(index)

    def sum(self, index):
        """
        Compute the sum of item in the range 0:index
        O(logN) running time complexity.
        :param index: the end range
        :return: the sum of item
        """

        # index start with 0, but the Fenwick tree start from 1
        index += 1

        sum = 0

        # consider the sum of multiple ranges until the parent of the three
        while index > 0:
            sum += self.fenwick_tree[index]

            # go to the parent index and keep going
            index = self.parent(index)

        return sum

    def range_sum(self, start, end):
        """
        Compute the sum of item for the given range start:end
        O(logN) running time complexity.
        :param start: begin index
        :param end: end index
        :return: sum of item
        """
        return self.sum(end) - self.sum(start - 1)


if __name__ == "__main__":

    nums = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]

    fenwick_tree = FenwickTree(nums)


    print("sum of 0-10: {}".format(fenwick_tree.sum(10)))

    print("sum of 2-5: {}".format(fenwick_tree.range_sum(2, 5)))