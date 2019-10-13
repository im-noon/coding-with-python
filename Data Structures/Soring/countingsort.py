"""
Counting sort:
- It operates by counting the number of objects that have each distinct key
  value.
- Integer sorting algorithm: we assume the values to be integers.
- And using algorithmic on those counts to determine the position of each key
  value in the output sequence.
- It us only work for direct use in situations where the variation in keys is
  not significantly greater that the number of items.
- It can be use as subroutine of radix sort.
- Running time O(N + k), where
    -> N: the number of items we want to sort,
    -> k: different between the maximum and minimum keys values, basically
    the number of possible keys.
- Conclusion: it is on ly suitable for direct use in situations where the
  variation in keys us not significantly greater than the numbers of items.

Pseudo code:
countingSort(array, min, max)
    count_array = new array with size [max - min + 1]

    for i in array
        increment count_array[i-min]

    z = 0

    for i in count_array.length
        while count_array[i-min] > 0
            array[z] = i
            z++
            count_array[i-min] = count_array[i-min] - 1

"""

def counting_sourt(nums, max):
    counts = [0 for  _ in range(max + 1)]
    for i in nums:
        counts[i] = counts[i] + 1

    z = 0

    for i in range(len(counts)):
        while counts[i] > 0:
            nums[z] = i
            z += 1
            counts[i] -= 1


if __name__ == "__main__":

    array = [23, 6, 4, 1, 0, 12, 8, 3, 1]
    print(array)
    maximum = max(array)
    counting_sourt(array, maximum)
    print(array)