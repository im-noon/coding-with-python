"""The problem is that we want to find duplicates in a one-dimensional
array of integers in O(N) running time where the integer
values are smaller than the length of the array!
"""

def duplicate_array(arr):
    for num in arr:
        if arr[abs(num)] >= 0:
            arr[abs(num)] = -arr[abs(num)]
        else:
            print("Repetition found :{}".format(abs(num)))

if __name__ == "__main__":
    array = [2, 6, 5, 1, 4, 3, 2]
    duplicate_array(array)