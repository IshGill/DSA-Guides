def trapping_rainwater(height):
    dpLeft = []
    dpRight = []
    maxRight = 0
    maxLeft = 0
    for i in range(len(height)):
        maxLeft = max(height[i], maxLeft)
        dpLeft.append(maxLeft)

    for i in range(len(height)-1,-1,-1):
        maxRight = max(height[i],maxRight)
        dpRight.append(maxRight)
    dpRight.reverse()

    for i in range(len(dpLeft)):
        dpLeft[i] = (min(dpLeft[i], dpRight[i]) - height[i])
    return sum(dpLeft)

print(trapping_rainwater([0,1,0,2,1,0,1,3,2,1,2,1]))
