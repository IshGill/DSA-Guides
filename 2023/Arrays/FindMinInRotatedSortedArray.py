# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

def inflectionPointPattern(nums):
    # If the element at the 0th index is <= the element at the end of the array, then the array has NOT been rotated so return the first value
    # As the first value IS the minimum value
    # [1,2,3,4,5] implies n[0] <= n[-1] implies 1 <= 5 implies array HAS NOT been rotated
    # [5,1,2,3,4] implies n[0] <= n[-1] implies 5 > 4 implies array HAS been rotated
    # [2,3,4,5,1] implies n[0] <= n[-1] implies 2 > 1 implies array HAS been rotated
    if nums[0] <= nums[-1]:
        return nums[0]
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # If value behind/prior to the current value is GREATER THAN the current value, this implies that the current value is the inflection point
        # This is because that remember the array is in sorted order, so even if it has been rotated, if you ever arrive at an instance where
        # nums[i-1] > nums[i] then nums[i] is the inflection point
        # [2,3,4,5,1], nums[i] = 1, then nums[i-1] = 5, then nums[i-1] > nums[i] then nums[i] MUST be the inflection point as there can only ever
        # be one such occurence in the rotated sorted array!  
        if nums[(mid-1)%len(nums)] > nums[mid]:
            return nums[mid]
        # If value at the current index is greater than the value at the i+1th index, then clearly, given this is a sorted array the value at the 
        # i+1th index is the inflection point! 
        # [3,4,5,1,2], given nums[i] = 5, then nums[i+1] = 1, then nums[i] > nums[i+1] but because the array is sorted this should be impossible! 
        # However the array is rotated and all this implies is that the i+1th index element is the inflection point! 
        elif nums[mid] > nums[(mid+1)%len(nums)]:
            return nums[(mid+1)%len(nums)]
        # If the element at the current mid index is greater than the element at the start of the array, then we can say that up till this point 
        # in the array it is in proper sorted order so we just go right.
        # [2,3,4,5,1], mid = 4, nums[0] = 2, therefore 4 > 2, hence nums[0:mid] is in proper sorted order so we go right! 
        elif nums[mid] > nums[0]:
            left = mid + 1
        # If the element at the current mid index is LESS THAN the element at the 0th index, the start of the array, this implies that the rotated
        # portion of the array falls within nums[0:mid], this implies that the smallest element falls within this subarray too, so we need to go 
        # left
        # [5,1,2,3,4]
        else:
            right = mid - 1

# MAIN KEY FOR GOING LEFT AND RIGHT IN THE ROT
# TO GO LEFT IN ARRAY FOR BINARY SEARCH WE DO RIGHT = MID -1 
# TO GO RIGHT IN ARRAY FOR BINARY SEARCH WE DO LEFT = MID + 1

print(inflectionPointPattern([1,2,3,4,5]))
print(inflectionPointPattern([5,1,2,3,4]))
print(inflectionPointPattern([2,3,4,5,1]))
print(inflectionPointPattern([2,1]))

