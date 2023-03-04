# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Kadanes algorthm 
# The max subarray is either N or N + M at any given element N
# [-2,1,-3,4,-1,2,1,-5,4]
def maxSubarray(nums):
    local_max = nums[0]
    global_max = nums[0]
    for i in nums[1:]:
        local_max = max(i, local_max + i)
        global_max = max(global_max, local_max)
    return global_max

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))