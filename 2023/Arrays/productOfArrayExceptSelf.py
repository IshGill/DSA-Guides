# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# [1, 1, 2, 6] = LEFT PASS ARRAY 
# [24, 12, 4, 1] = RIGHT PASS ARRAY
# [24, 12, 8, 6] = Final array 

def productExceptSelf(nums):
    ans = [1] * len(nums)
    product = 1
    for i in range(len(nums)):
        ans[i] = product
        product *= nums[i]
    
    product = 1
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= product
        product *= nums[i]
    return ans

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
