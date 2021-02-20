# Dynamic sliding window, two pointer approach, apply x + y + z = 0 formula nice and easy!
def threeSum(nums):
    triples = []
    # We need to sort before doing any 2sum, 3sum approach using dynamic window
    nums.sort()
    # We use len - 2 because we need at least 3 numbers to continue
    for i in range(len(nums) - 2):
        # This is how we can check for duplicates and avoid them! THIS IS MUCH MORE EFFICIENT THAN USING A SET!
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        windowStart = i + 1
        windowEnd = len(nums) - 1
        while windowStart < windowEnd:
            target = nums[i] + nums[windowStart] + nums[windowEnd]
            if target < 0:
                windowStart += 1
            elif target > 0:
                windowEnd -= 1
            else:
                triples.append((nums[i], nums[windowStart], nums[windowEnd]))
                # These two while loops will avoid the duplicates for both windows!
                while windowStart < windowEnd and nums[windowStart] == nums[windowStart + 1]:
                    windowStart += 1
                while windowStart < windowEnd and nums[windowEnd] == nums[windowEnd - 1]:
                    windowEnd -= 1
                windowStart += 1
                windowEnd -= 1
    return triples

print(threeSum([-1,0,1,2,-1,-4]))

# IMPORTANT NOTES!
# If we need to check 3 elements in an array we must use len(array) -2, if we need to check only two elements we use len(array) -1 and follow this pattern
# USING CONTINUE MEANS YOU SKIP THE ITERATION OF THE FOR LOOP!
# Use if i > 0 and nums[i] == nums[i-1]: continue to check for duplicates!

# class Solution(object):
#     def threeSum(self, n):
#         triples = []
#         n.sort()
#         for i in range(len(n)-2):
#             if i > 0 and n[i] == n[i-1]:
#                 continue
#             windowStart = i + 1
#             windowEnd = len(n) - 1
#             while windowStart < windowEnd:
#                 target = n[windowStart] + n[windowEnd] + n[i]
#                 if target == 0:
#                     triples.append((n[windowStart],n[windowEnd],n[i]))
#                     while windowStart < windowEnd and n[windowStart] == n[windowStart + 1]:
#                         windowStart += 1
#                     while windowStart < windowEnd and n[windowEnd] == n[windowEnd - 1]:
#                         windowEnd -= 1
#                     windowStart += 1
#                     windowEnd -= 1
#                 elif target > 0:
#                     windowEnd -= 1
#                 else:
#                     windowStart += 1
#         return triples