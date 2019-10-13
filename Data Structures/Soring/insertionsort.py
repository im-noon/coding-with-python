"""
Insertion sort:
- It is a simple sorting algorithm that builds the final sorted array one
item at a time.
- It has running time complexity O(N^2)
- On large dataset it is very inefficient, but on small arrays(10-20) element
it is quite good.
- Simple implementation!!!
- It is more efficient that other quadratic running time sorting procedures
such as bubble sort or selection sort,
- It is an adaptive algorithm, speed up when array is already substantially
sorted.
- It is stable sort, preserve the order of the items with equal keys.
- It is in-place algorithm, does not need any additional memory.
- It is an online algorithm, it can sort an array as it receives it,
for example downloading data from the web.
- Hybrid algorithms user insertion sort if the subarray is small enough.
    >> insertion sort is faster for small subarray than quick sort!!!
- Variant of insertion sort is shell sort.
- Sometimes selection sort is better, they are very similar algorithm.
- Insertion sort requires more writes because the inner loop can require
shifting large sections of the sorted portion if the array.
- In general, insertion sort will write to the array O(N^2) times,
while selection sort will write only O(N) times.
- For this reason, selection sort can be preferable in case where writing to
memory is significant more expensive than reading
    >> for example, flash memory.

Pseudo code:
function insertionSort(array)
    for i = 1 to array.length
        j = i
        while j > 0 and array[j-1] > array[j]
            swap(array, j, j-1)
            j = j - 1
"""

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            swap(nums, j, j - 1)
            j -= 1

    return nums

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

if __name__ == "__main__":
    array = [55, -2, 34, 10, 0, 2, -5, 12]
    print(insertion_sort(array))