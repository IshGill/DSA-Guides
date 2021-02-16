def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hash_Table = {i: [] for i in nums}
    [hash_Table[i].append(i) for i in nums]
    for key, value in hash_Table.items():
        if len(value) <= 1:
            return key

nums = [2,2,1]
print(singleNumber(nums))
# Output: 1

nums = [4,1,2,1,2]
print(singleNumber(nums))
# Output: 4

nums = [1]
print(singleNumber(nums))
# Output: 1