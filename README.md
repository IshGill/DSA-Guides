# DSA and Leetcode walkthroughs 
My walkthroughs, designed to help build solid fundamentals and understanding for concepts in data structures and algorithms, and how to identify patterns and efficiently solve various leetcode problems.  

# Patterns
## Sliding Window
Use the sliding window pattern whenever you need to work with arrays, linked lists or any data structure where the elements need to be iterated through in a contiguous order. Sliding window works well as we visit the elements only once hence avoid duplicates or constantly revisiting elements as seen with brute force approaches. The main takeaway here should be that the sliding window pattern should be the first thing which comes to mind when doing anything which involves subsets of any given set ie subarrays of an array.
## Fixed length sliding window problem - Maximum sum for a length 3 subarray in a given array
Fixed length sliding window means that the windows size does not change, hence, the subarray size we are looking at will never change, we are always looking at the same number of elements. For this problem all we need to do is once our sliding window hits the fixed size given in the question we simply increment both window_start and window_end and take the max of each contiguous fixed window until we reach the end of the array.
![1](https://user-images.githubusercontent.com/57751792/108481644-51d2e480-72fd-11eb-925b-d12417425922.jpg)

    def minSubArrayLen(target, nums):
        min_window_size = 2 ** 31 - 1
        current_window_sum = 0
        window_start = 0
        flag = False
        for window_end in range(len(nums)):
            current_window_sum += nums[window_end]
            while current_window_sum >= target:
                min_window_size = min(min_window_size, window_end - window_start + 1)
                current_window_sum -= nums[window_start]
                window_start += 1
                flag = True
        return min_window_size if flag == True else 0
        
## Dynamic sized sliding window problem - Container with most water
Dynamic sized sliding windows have no fixed length they are altered in respect to the given conditions of the problem. A dynamic sized sliding window works well for this problem as, what we need to do is have two pointers, I like to refer to them as windowStart and windowEnd. Starting from the beginning and end of the array we adjust our two pointers hence our dynamic window in order to find the largest area of the container. The formula is simply area = width x height, where height is the minimum value between the elements which are at the windowStart and windowEnd indexes in the array. The width is the distance between these elements, given as windowEnd - windowStart. 

    def maxArea(height):
        maxSum = 0
        windowStart = 0
        windowEnd = len(height) - 1
        while windowStart < len(height):
            runningSum = min(height[windowStart], height[windowEnd]) * (windowEnd - windowStart)
            maxSum = max(maxSum, runningSum)
            if height[windowEnd] < height[windowStart]:
                windowEnd -= 1
            else:
                windowStart += 1
        return maxSum

## Sliding window problem - Length of longest substring with non-repeating characters
The idea for this algorithm is if we add every element in our window into our set, if we come across the same element we have a duplicate somewhere we keep removing elements from the set until the duplicate issue is rectified, finally as we are adding elements to our set, we are recording the MAX length of the set, we return the max length the set was hence the longest non-repeating substring.

    def lengthOfLongestSubstring(s):
        # Starting window index
        windowStart = 0
        # Ending window index
        windowEnd = 0
        # Our running sum which holds the max subarray(window size) which is a set of substring of our string without repetitions
        running_sum = 0
        # Our hash set which will hold the characters without holding any repeats
        hash_set = set()
        while windowEnd < len(s):
            # We need to stop when the end window index reaches the end of the array
            if s[windowEnd] not in hash_set:
                # If the current element we are looking at is not in the set, add it to the set.
                hash_set.add(s[windowEnd])
                # Increase the size of our window
                windowEnd += 1
                # Update the running_sum to hold the new max window size, if the new size is less of course we will stick with the previous max window size of running sum
                running_sum = max(running_sum, len(hash_set))
            else:
                # Else, if we have come across a repetition, this means that the current element we are looking at with s[windowEnd] is already in our hash_set, so we are going to remove the first element
                # in our hash set, thus incrementing our window as we don't want the repeats, we keep doing this until that repeat is gone
                hash_set.remove(s[windowStart])
                # This will make the size of our window smaller
                windowStart += 1
        return running_sum

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
