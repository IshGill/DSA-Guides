# We use a greedy backtracking approach. It is quite simple.
# Given [2, 3, 1, 1, 4] all we want to do is start from the last index element in the array, hence the target.
# We are just going to go backwards and check if we are able to reach the previous element, hence the element we just came from.
# This means that if we can get to the 0th index from the end we are able to reach the last element in the list, else we are not.
# ie [2, 3, 1, 1, 4], start at 4, i + nums[i] = 4 + 4 > lastgoodindex = 4 is reachable, therefore move down the list, update lastgoodindex to be i
# Now i moves to 3. i + nums[i] = 3 + nums[3] = 3 + 1 >= lastgoodindex = 3 is reachable, therefore move down and make lastgoodindex the next element so i = 2
# i moves to 2. i + nums[i] = 2 + nums[2] = 2 + 1 >= lastgoodindex = 2 is reachable, therefore move down and make lastgoodindex the next element so i = 1
# i moves to 1. i + nums[i] = 1 + nums[1] = 1 + 3 >= lastgoodindex = 1 is reachable, update lastgoodindex to i = 0
# i moves to 0. i + nums[i] = 0 + nums[0] = 0 + 2 >= lastgoodindex = 0 is reachable. We are done. 
def canJump(nums):
    lastGoodIndex = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= lastGoodIndex:
            lastGoodIndex = i
    return True if lastGoodIndex == 0 else False