"""
Radix sort:
- Can be very efficient, because there are not comparisons.
- So running time complexity can be reach O(N).
- Running time O(k*N), where k is the number of digits in the input.
- Sort elements according to individual characters
- It is stable algorithm.

LSD string sorting:
- Least-significant-digit-first string sorting.
- Consider character from right to left.
- We can use it to fixed length strings or fixed length numbers for
  example integers.
- Sort the characters at least column... then keep going left and sort the
  columns independently.
MSD string sort:
- Most-significant-digit-first string sorting.
- Consider characters from left to right.
- It is sensitive to ASCII and Unicode representations.
- Is has several advantages:
    -> MSD examines just enough characters to the soring key
    -> Can be sublinear in input size!!!
- MSD access memory randomly, not so efficient.
- We should combine it with quick sort... this is 3-way radix quick sort.
"""


def radixSort(arr):
    # Find the maximum number to know number of digits
    maximum = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while maximum / exp > 0:
        counting_sourt(arr, exp)
        exp *= 10

def counting_sourt(arr , exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] // exp1)
        count[(index) % 10] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

if __name__ == "__main__":

    array = [170, 45, 75, 90, 802, 24, 2, 66]
    print(array)
    radixSort(array)
    print(array)
