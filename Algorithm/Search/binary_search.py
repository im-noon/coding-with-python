"""
Binary search:
- If array is sorted, wa can use binary search  as reduce the running time
complexity to O(logN)
"""

def binary_search(arr, item, left, right):

    # base case, missing item
    if left > right:
        return -1

    middle = (left + right) // 2
    print("middle index :{}".format(middle))

    if arr[middle] == item:
        return middle

    # the looking item smaller then the middle item
    if left < middle:
        print("Checking item on left side...")
        return binary_search(arr, item, left, middle - 1)

    # the looking item greater that the middle item
    else:
        print("Checking item in the right...")
        return binary_search(arr, item, middle + 1, right)


if __name__ == "__main__":
    array = [1, 4, 7, 8, 9, 10, 11, 20, 22, 25]
    print(binary_search(array, 44, 0, len(array) - 1))