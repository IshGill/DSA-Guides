def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) <= 1:
        return False
    return True if len(nums) != len(set(nums)) else False

print(containsDuplicate([1,2,3,1]))
# Output: true

print(containsDuplicate([1,2,3,4]))
# Output: false

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
# Output: true