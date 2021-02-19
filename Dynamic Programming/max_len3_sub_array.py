# Fixed size window
def max_sub_array(array, k):
    running_sum = 0
    maxValue = -2**31

    # We iterate the entire length of the array
    for i in range(len(array)):
        # Build our running sum value with each iteration
        running_sum += array[i]
        # If i >= k-1 this means we have our window
        # We do k-1 to account for the fact that we are using len(list)
        if i >= k-1:
            # Find the max value between the current window and the running sum window which changes as we go
            maxValue = max(maxValue, running_sum)
            # We remove the first element in the window from our running sum, hence we deduct it. We do this because we want to
            # continue to "slide" our window along the array, hence removing one element from the front leaving us with 2
            # then adding one element to the end hence giving us one again, the continuously checking the sum of each new consecutive window
            running_sum -= array[i-(k-1)]
    return maxValue

print(max_sub_array([4,2,1,7,8,1,2,8,1,0], 3))

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

