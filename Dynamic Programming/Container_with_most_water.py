# Dynamic sliding window where we adjust both end accordingly and all we are doing is finding the max area so w x h between the start of the window and end of the windows
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

    # for windowStart in range(len(height)-1):
    #     runningSum = min(height[windowStart], height[windowEnd]) * (windowEnd - windowStart)
    #     maxSum = max(maxSum, runningSum)
    #     while height[windowEnd] < height[windowStart]:
    #         runningSum = min(height[windowStart], height[windowEnd]) * (windowEnd - windowStart)
    #         maxSum = max(maxSum, runningSum)
    #         windowEnd -= 1
    # return maxSum