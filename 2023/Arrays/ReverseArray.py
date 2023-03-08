def reverseArray(nums):
    right = len(nums)-1
    if len(nums) % 2 == 0:
        mid = len(nums) // 2 
    else:
        mid = (len(nums) // 2) + 1 
    for i in range(mid):
        temp = nums[i]
        nums[i] = nums[right-i]
        nums[right-i] = temp

nums_list = [1,2,3,4,5]
reverseArray(nums_list)
print(nums_list)