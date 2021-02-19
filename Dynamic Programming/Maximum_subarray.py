# Dynamic window
# Kadane's Algorithm
# Ok, we want to find the largest possible contiguous subarray from a given array. What Kadane's algortihm does is like a dynamic sliding window approach
# What's happening is, we have two variables, current and global maximums, pretty much current is the current size of the dynamic window and global is the max
# recorded size of the dynamic window. So, whats going to happen is as we iterate through the array, find the current_max sub array or better think of it as the current
# max dynamic window. We check, is my current sub array or current element greater than the current element plus the previous sub array. If our current element is greater
# we stick with that elements, else our current element plus the previous sub array elements with dynamic window of size x is greater. So what this implies is simply, each iteration
# we are building up our largest sub array, we have our initial global max right, then we uodate once most likely, then as we keep building up our local_max we keep updating the global max

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