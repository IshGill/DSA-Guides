# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

def containsDuplicate(nums):
    dict = {}
    for i in nums:
        if i not in dict:
            dict[i] = 0
        else:
            dict[i] += 1
    if sum(dict.values()) == 0:
        return False
    else:
        return True

print(containsDuplicate([1,2,3,1]))

def containsDuplicateOneLiner(nums):
    return len(set(nums)) != len(nums)

print(containsDuplicateOneLiner([1,2,3,1]))