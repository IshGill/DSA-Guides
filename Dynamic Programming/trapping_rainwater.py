#* Idea is the list in question "height" depcits the possible water levels at each specific index.
#* What we are going to do is find the height of the each "building" at each index in the given "height" array
#* How we do this is we make to dp (dynamic programming) lists, we parse left and append only the max values of each consecutive index to the list
#* We parse right and append the max element values for all indexes to the dpRight list. NOTE WITH DPRIGHT WE MUST REVERSE THE LIST
#* Finally we are going to take the min of the correpsonding values in both of these lists and store that in either or dpLeft or dpRight list, does not really matter
#* BUT the main idea will be we must deduct the corresponding height indexes to! Recall the height list depicts the possible water level.
#* It all comes together here! So the min of dpLeft and dpRight will give us the index of the buildings, the corresponidng height index gives us the value of possible water levels at each corresponding index
#* Hence, if we deduct the building height from the possible water level we get the water level for that specific index.
#* Therefore, dpLeft will be left with just the total possible water levels from each given index from the list in question, so just return the sum of its values for the total water level. Done!
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