# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# O(n logn) = sort the array and count the consecutive sequence
# O(n) convert the array to a set. 

def countSeq(nums):
    nums_set = set(nums)
    max_sequence = 1
    for i in nums_set:
        if i-1 not in nums_set:
            count = 1
            sequence = i+1
            while sequence in nums_set:
                count += 1
                sequence += 1
            max_sequence = max(max_sequence, count)
    return max_sequence

print(countSeq([0,3,7,2,5,8,4,6,0,1]))