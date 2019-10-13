"""
Selection sort:
- Another O(N^2) sunning time sorting algorithm
- Selection sort is noted for its simplicity and it has performance
advantages over more complicated algorithms.
- Particularly useful where auxiliary memory limited.
- The algorithm divides the input its into two parts:
    * the subarray of items already sorted
    * and the subarray of items remaining to be sorted that occupy the rest
    of the array.
How it work:
- The algorithm proceeds by finding the smallest element in the unsorted
subarray.
- Exchange/ swap it with the leftmost unsorted element -> putting it in
sorted order.
- Moving the subarray boundaries on element to the right.
- It is an in-place algorithm -> no need more extra memory
- Selection sort almost always outperforms bubble sort.
- Not stable sort -> does not preserve the order of key with equal values.
Pseudo code:
function selectionSort(array)
    for i in range array.length - 1
        index = i

        for j from i + 1 to array.length - 1
            if array[j] < array[index]
                index = j

        if index not i
            swap(array, index, i)
"""
def selection_sort(nums):

    for i in range(len(nums) - 1):
        index = i
        for j in range(i + 1, len(nums) - 1):
            if nums[j] < nums[index]:
                index = j
        if index != i:
            swap(nums, index, i)
    return nums

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

if __name__ == "__main__":
    array = [-1, -3, -2, 0]

    print(selection_sort(array))
