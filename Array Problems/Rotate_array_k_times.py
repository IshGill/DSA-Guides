def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # for i in range(len(nums)):
    #     nums.insert(0, nums.pop())
    #     k -= 1
    #     if k == 0:
    #         return nums

    #Better way
    return [nums.insert(0, nums.pop()) for i in range(k)]

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

nums = [-1,-100,3,99]
k = 2
print(rotate(nums, k))
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

