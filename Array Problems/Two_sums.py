def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_table = {}
    for index, element in enumerate(nums):
        what_i_need = target - element
        if what_i_need in hash_table:
            return [hash_table[what_i_need], index]
        else:
            hash_table[element] = index

nums, target = [2,7,11,15], 9
print(twoSum(nums,target))
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

