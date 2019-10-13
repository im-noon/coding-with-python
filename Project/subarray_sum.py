"""
Create an algorithm to find the sum of contiguous subarray
within a one-dimensional array of numbers which has the largest sum!
"""
def kadane_algorthm(nums):
    local_maximum = nums[0]
    global_maximum = nums[0]

    for i in range(len(nums)):
        local_maximum = max(nums[i], local_maximum + nums[i])
        if local_maximum > global_maximum:
            global_maximum = local_maximum

    return global_maximum

if __name__ == "__main__":
    nums = [1, -2, 3, 4, -5, 8]
    print(kadane_algorthm(nums))