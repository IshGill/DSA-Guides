def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if nums[left] > target:
                left = mid + 1
            else:
                right = mid 
        elif nums[mid] < target:
            if nums[right] < target:
                right = mid - 1
            else:
                left = mid + 1
    return -1
        
    # # find point of inflection 
    # def getInflectionPoint(nums):
    #     l = 0
    #     r = len(nums) - 1
    #     while l < r:
    #         m = (l + r) // 2
    #         if nums[m] > nums[r]:
    #             l = m + 1
    #         elif nums[m] <= nums[r]:
    #             r = m
    #     return l
    # inflection_point = getInflectionPoint(nums)
    
    # l = 0
    # r = len(nums) - 1
    # while l <= r:
    #     m = (l + r) // 2
    #     if nums[m] == target:
    #         return m
    #     elif 

print(search([4,5,6,7,0,1,2], 0))
print(search([5, 6, 7, 1, 2, 3, 4], 7))