# Main idea is we think of lower and upper being included in the array
# 1: We set prev as lower - 1 as we do not want to include the given ranges in the output
# *2: Make sure the for loop range is len(nums) + 1 as we want to grab and use the upper range value in the last iteration
# *3: Every iteration compare the previous value + 1 with the current value - 1 this checks if there is indeed a valid range between the two elements
# *4: If this condition is true then we may only have one value between them so we call a helper function to do this check and return the correctly formatted result
# *5: Set previous to current each iteration as we increment current hence we can compare with each new element in the array, think of this as sliding a fixed size window across
def findMissingRanges(nums, lower, upper):
    ranges = []
    windowEnd = lower - 1
    for i in range(len(nums) + 1):
        windowStart = nums[i] if i < len(nums) else upper + 1
        if windowEnd + 1 <= windowStart - 1:
            ranges.append(formatStr(windowEnd + 1, windowStart - 1))
        windowEnd = windowStart
    return ranges

def formatStr(windowEnd, windowStart):
    return str(windowEnd) if windowEnd == windowStart else str(windowEnd) + "->" + str(windowStart)