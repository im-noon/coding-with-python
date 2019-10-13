"""
Linear search:
- If we want to find a given in an array by consider all the items one by one
  with the linear running time complexity O(N)
"""

def linear_search(arr, item):

    for i in range(len(arr)):
        if arr[i] == item:
            return i

    return -1

if __name__ == "__main__":
    arr = [1, 4, 7, 3, 6, 8, 11, 10, 20, 22]
    item = 30
    print("linear search {} found at index {}".format(item, linear_search(
        arr, item)))

    item = 20
    print("linear search {} found at index {}".format(item, linear_search(
        arr, item)))