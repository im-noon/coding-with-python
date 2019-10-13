"""
The problem is that we want to reverse a T[] array in O(N)
 linear time complexity and we want the algorithm to be in-place as well!

For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]
"""

# in-place algorithm with linear running time O(N)
def reverse_array(arr):

    # pointer to the first and last item
    start_index = 0
    end_index = len(arr) - 1

    # iterate until start_index < end_index
    while start_index < end_index:
        # swap two array
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        # increment start index
        start_index += 1

        # decrement end index
        end_index -= 1

    return arr

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    print(reverse_array(array))
