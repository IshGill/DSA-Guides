def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums[:] = sorted(set(nums))
    return len(nums)

nums = [1,1,2]
print(removeDuplicates(nums))
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
# Output: 5, nums = [0, 1, 2, 3, 4]
# Explanation: Your
# function
# should
# return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.It doesn't matter what values are set beyond the returned length.
