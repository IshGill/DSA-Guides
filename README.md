# DSA and Leetcode walkthroughs 
My walkthroughs, designed to help build solid fundamentals and understanding for concepts in data structures and algorithms, and how to identify patterns and efficiently solve various leetcode problems.  

# Strings
## License Key Formatting 
All we need to do with this question is firstly clean up the given string S by making it uppercase and replacing all instances of - with empty strings.
Now, the main trick to solving this problem is the fact that the first grouping can have any number of elements, hence this is why we need to work FROM THE END of the string. As all we really need to do is split the string into groups of size K, however the first group can be any size aslong as the rest are size K, meaning the first group is like the leftovers which we get from splitting the string into K units! Therefore, all we need to do to solve this problem is run a simple string splitting for loop, BUT FIRST REVERSE THE LIST, because we want to our leftovers which are not a full K units to be the first alphanumeric characters in the string. Finally, after completing the splitting process return the string reversed again, hence in the original order. 

    def licenseKeyFormatting(self, S, K):
        S = S.replace('-','').upper()[::-1]
        #Replace the dashes, go uppercase, reverse the string
        new_S = []
        #Break the string into K units append each unit to new list
        for i in range(0, len(S), K):
            new_S.append(S[i:i+K])
        #Join the new list and return in after reversing! 
        return "-".join(new_S)[::-1]
# Arrays
# LinkedLists
# Sorting & Searching
# Stacks
# Queues
# Priority Queues/Heaps
# Trees
# Hash tables
# Dynamic Programming 
## Kadane's Algorithm - Maximum Subarray
The way to approach the maximum Subarray problem is by using Kadane's algorithm. How Kadane's algorithm works is, we start off with the first index element in the array. We set our current max and global max to this element. We then want to iterate through the remainder of the array, we want to build up the sum in our current max variable. However, what we are going to do is always take the maximum between the current array elemet (list[i]) and the current array element plus whatever we have in our current sub array so (list[i] + current_max). This was we only take the maximum sub array in each iteration, this is how we build up our current maximum sub array. Then each iteration, we ask is the current sum of our current_max subarray LARGER than the sum in the global_max subarray? We the update accordingly. Finally we are left with the largest subarray sum in global_max. 

    def maxSubArray(nums):
        # Initalize two variables, current and global max to point at the first element in the array
        current_max = global_max = nums[0]
        #Iterate from the 1st index in the array till the end, we skip the 0th index because we are already looking at it with curret_max and global_max
        for i in range(1, len(nums)):
            # Every iteration, we ask, is the current array value greater than the current array value plus the previous array value, we ask this ofcourse as there may be negative elements
            # Which decrease our total maximum sum, which we do not want, we want the maximum.
            current_max = max(nums[i], nums[i] + current_max)
            # Next we keep updating our global maximum aslong as current_max is growing!
            if current_max > global_max:
                global_max = current_max
        return global_max
