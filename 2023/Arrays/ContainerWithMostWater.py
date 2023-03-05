def maxArea(height):
    ws = 0
    we = len(height) - 1
    max_area = 0
    while ws < we:
        width = we - ws
        min_height = min(height[ws], height[we])
        area = width * min_height
        max_area = max(max_area, area)
        if height[ws] < height[we]:
            ws += 1
        else:
            we -= 1
    return max_area
