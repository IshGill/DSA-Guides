# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

def trapWater(heights):
    left_subarray = [0] * len(heights)
    right_subarray = [0] * len(heights)
    max_left = heights[0]
    max_right = heights[-1]
    water = 0
    for i in range(1, len(heights)):
        left_subarray[i] = max_left
        max_left = max(max_left, heights[i])
    for i in range(len(heights)-2, -1, -1):
        right_subarray[i] = max_right
        max_right = max(max_right, heights[i])
    for i in range(1, len(heights)-1):
        min_max_value = min(left_subarray[i], right_subarray[i])
        water += max(0, min_max_value - heights[i])
    return water

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapWater(heights))