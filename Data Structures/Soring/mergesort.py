"""
 Merge sort:
 - Merge sort is the divide and conquer algorithm, that was invented
 by John Neumann in 1945
 - It is comparison based algorithm with running time complexity O(N logN)
 - It is a stable sorting algorithm
 - Not in-place algorithm!!!
 - Although heap sort has the same time bounds as merge sort
    -> heap sort require only O(1) space complexity instead merge sort's O(n)
 - Efficient quick sort implementations general outperforms merge sort
 - Merge sort id often the best choice for sorting a linked list: in this
  situation it is relatively easy to implement a merge sort in such a way that
  it require on O(n) extra space.
 How it worK:
 1. divide the array into two subarray recursively
 2. sort these subarray recursively with merge sort again
 3. if there is only a single item left in the subarray, we consider it to be
    sorted by definition.
 4. merge the subarray to get the final sorted array.
 Pseudo code:
    mergeSort(array, low, height)
        if low >= height
            return
        middle = (low + height)/2

        mergeSort(array, low, middle)
        mergerSort(array, middle + 1, height)
        merge(array, low, middle, height)

    merge(array, low, middle, height)
        for i = low to height
            temp[i] = array[i]

        i = low
        j = middle + 1
        k = low

        while i < middle && j < height
            if temp[i] <= temp[j]
                array[k] = temp[i]
                i++
            else
                array[k] = temp[j]
                j++
            k++

        // copy remaining left sorted array
        while i < middle
            array[k] = temp[i]
            k++
            i++

        // copy remaining right sorted array
        while j < height
            array[k] = temp[j]
            k++
            j++
"""
def merge_sort(nums):
    if len(nums) == 1:
        return

    middle_index = len(nums)//2

    left_array = nums[:middle_index]
    right_array = nums[middle_index:]

    merge_sort(left_array)
    merge_sort(right_array)
    merge(nums, left_array, right_array)

def merge(nums, left_array, right_aray):
    i = 0
    j = 0
    k = 0
    while i < len(left_array) and j < len(right_aray):
        if left_array[i] < right_aray[j]:
            nums[k] = left_array[i]
            i += 1
        else:
            nums[k] = right_aray[j]
            j += 1
        k += 1

    while i < len(left_array):
        nums[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_aray):
        nums[k] = right_aray[j]
        j += 1
        k += 1

if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    print(array)
    merge_sort(array)
    print(array)