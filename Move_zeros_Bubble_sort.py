def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # Very inefficient but a cool way to implement bubble sort
    for i in range(1, len(nums)):
        for n in range(len(nums) - 1):
            if nums[n] == 0 and nums[n + 1] != 0:
                nums[n], nums[n + 1] = nums[n + 1], nums[n]
    return nums

Input = [0,1,0,3,12]
print(moveZeroes(Input))
# Output: [1,3,12,0,0]