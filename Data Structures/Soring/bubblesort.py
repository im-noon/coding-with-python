"""
Bubble sort:
- Repeatedly steps through the list to be sorted, compares each pair of
  adjacent items and swaps then if they are in the wrong order.
- It is to slow and impractical for most problems event when compared to
  insertion sort.
- Bubble sort has worst case and average complexity both O(N^2)
- Bubble sort is not practical sorting algorithm.
- It will not be efficient in the case of a reverse-ordered collection.
- It is a stable sorting algorithm,
- It is an in-place algorithm, does not need any additional memory.
Pseudo code:
function bubbleSort(array)
    for i in range array.length - 1
        for j in range array.length - 1
            if array[j]> array[j+1]
                swap(array, j, j + 1)
"""

def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[j]> nums[j + 1]:
                swap(nums, j, j + 1)

def swap(nums,i, j):
    nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    array = [4, 1, 3, 2]

    bubble_sort(array)

    print(array)