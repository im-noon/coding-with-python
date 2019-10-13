"""
Quick sort:
- It is developed by Tony Hoare in 1959
- It is efficient sorting algorithm.
A well implemented quick sort can out performs heap sort and merger sort
- It is a comparison based algorithm, not able to faster than linearithmic
time complexity.
- The efficient implementation of quick sort in not stable.
- It is in-place, does not need additional memory.
- Average running time complexity O(N*logN)
- Wort case running time is quadratic O(N^2)
- It widely ise in programming languages:
    -> Primitive types, usually quick sort is used.
    -> Reference types/objects, usually merge sort is used.
- It is a divide and conquer algorithm.

How it work:
- pick element from  the array: this is call "pivot"
- partition phase: rearrange the array, so that all elements with values less
than the pivot came before the pivot, while all element with values greater
that the pivot com after it.// equal value can go either way
- recursively apply these steps on the sub array.
- Base case for recursion: arrays of size zero or one never need to be sorted.

Choose the pivot:
- It is important if we keep choosing bad pivot, the running time complexity
will be quadratic.
    >> we can choose pivot at random // this usually working fine
    >> choose the middle index of the array as the pivot

Pseudo code:

quickSort(array, low, height)
    if low >= height
        return
    pivot = partition(array, low, height)
    quickSort(array, low, pivot - 1)
    quickSort(array, pivot + 1, height)

partition(array, low, height)
    pivotIndex = (low + height)/2
    swap(pivotIndex, height)

    i = low

    for j = low to height
        if array[j <= array[height]
            swap(array, i, j)
            i++
    swap(i, height)

    return i // threshold index
"""
def quickSort(nums, low, height):
    if low > height:
        return

    pivot = partition(nums, low, height)
    quickSort(nums, low, pivot - 1)
    quickSort(nums, pivot + 1, height)

def partition(nums, low, height):
    pivot = (low + height) // 2
    swap(nums, pivot, height)
    i = low
    for j in range(low, height):
        if nums[j] <= nums[height]:
            swap(nums, i, j)
            i += 1
    swap(nums, i, height)
    return i

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

if __name__ == "__main__":

    array = [23, 6, 4, -1, 0, 12, 8, 3, 1]
    quickSort(array, 0, len(array) - 1)
    print(array)