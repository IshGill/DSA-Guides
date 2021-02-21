# DSA and Leetcode walkthroughs 
My walkthroughs, designed to help build solid fundamentals and understanding for concepts in data structures and algorithms, and how to identify patterns and efficiently solve various leetcode problems.  

# Patterns
## Sliding Window
Use the sliding window pattern whenever you need to work with arrays, linked lists or any data structure where the elements need to be iterated through in a contiguous order. Sliding window works well as we visit the elements only once hence avoid duplicates or constantly revisiting elements as seen with brute force approaches. The main takeaway here should be that the sliding window pattern should be the first thing which comes to mind when doing anything which involves subsets of any given set ie subarrays of an array.
## Fixed length sliding window problem - Maximum sum for a length 3 subarray in a given array
Fixed length sliding window means that the windows size does not change, hence, the subarray size we are looking at will never change, we are always looking at the same number of elements. For this problem all we need to do is once our sliding window hits the fixed size given in the question we simply increment both window_start and window_end and take the max of each contiguous fixed window until we reach the end of the array.
![1](https://user-images.githubusercontent.com/57751792/108481644-51d2e480-72fd-11eb-925b-d12417425922.jpg)
```
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
 ```       
## Dynamic sized sliding window problem - Container with most water
Dynamic sized sliding windows have no fixed length they are altered in respect to the given conditions of the problem. A dynamic sized sliding window works well for this problem as, what we need to do is have two pointers, I like to refer to them as windowStart and windowEnd. Starting from the beginning and end of the array we adjust our two pointers hence our dynamic window in order to find the largest area of the container. The formula is simply area = width x height, where height is the minimum value between the elements which are at the windowStart and windowEnd indexes in the array. The width is the distance between these elements, given as windowEnd - windowStart. 
```
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
```
## Sliding window problem - Length of longest substring with non-repeating characters
The idea for this algorithm is if we add every element in our window into our set, if we come across the same element we have a duplicate somewhere we keep removing elements from the set until the duplicate issue is rectified, finally as we are adding elements to our set, we are recording the MAX length of the set, we return the max length the set was hence the longest non-repeating substring.
```
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
```
## Dynamic window and hash map problem - Len of longest two distinct character substring
* Main idea for solving this one is a dynamic sliding window and hash table implementation. Here is the approach.
1. Start both the window pointers at the same index
2. Every iteration add the current element which the left pointer (the end window pointer) is currently pointing at. This guy is the one that moves down the string!
3. Once we have 3 distinct characters in our hash map (remember hash map keys cannot be duplicated!) then this means we need to delete the key of the value seen the longest time ago
4. What it means to delete the item seen "longest ago" is simply delete the item in your hash table which has the lowest corresponding string index value, hence the value to the key in the hash map
5. Of course, to do this operation with a hash map is simple, find the min value, then index into the corresponding key and do del hash_map[...]
6. Once we have deleted this element from the hash map, we now need to change the windows size, hence we need to bring the start of the window up to the point 1 index past the element we just deleted
7. So use the same variable (min value variable) and bring your windowStart up accordingly
8. Finally we do a check everytime to see if we have the longest distance between our string values which contain only 2 distinct characters, we add 1 to get the length between them.
```
def lengthOfLongestSubstringTwoDistinct(s):
    hash_map = {}
    windowStart = 0
    windowEnd = 0
    maxLen = 0
    while windowEnd < len(s):
        hash_map[s[windowEnd]] = windowEnd
        if len(hash_map) >= 3:
            find_min = min(hash_map.values())
            del hash_map[s[find_min]]
            windowStart = find_min + 1
        maxLen = max(maxLen, windowEnd - windowStart + 1)
        windowEnd += 1
    return maxLen
```
## Dynamic window - 3Sum
Dynamic sliding window, two pointer approach, apply x + y + z = 0 formula nice and easy!
IMPORTANT NOTES!
If we need to check 3 elements in an array we must use len(array) -2, if we need to check only two elements we use len(array) -1 and follow this pattern
USING CONTINUE MEANS YOU SKIP THE ITERATION OF THE FOR LOOP!
Use if i > 0 and nums[i] == nums[i-1]: continue to check for duplicates!
```
def threeSum(nums):
    triples = []
    # We need to sort before doing any 2sum, 3sum approach using dynamic window
    nums.sort()
    # We use len - 2 because we need at least 3 numbers to continue
    for i in range(len(nums) - 2):
        # This is how we can check for duplicates and avoid them! THIS IS MUCH MORE EFFICIENT THAN USING A SET!
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        windowStart = i + 1
        windowEnd = len(nums) - 1
        while windowStart < windowEnd:
            target = nums[i] + nums[windowStart] + nums[windowEnd]
            if target < 0:
                windowStart += 1
            elif target > 0:
                windowEnd -= 1
            else:
                triples.append((nums[i], nums[windowStart], nums[windowEnd]))
                # These two while loops will avoid the duplicates for both windows!
                while windowStart < windowEnd and nums[windowStart] == nums[windowStart + 1]:
                    windowStart += 1
                while windowStart < windowEnd and nums[windowEnd] == nums[windowEnd - 1]:
                    windowEnd -= 1
                windowStart += 1
                windowEnd -= 1
    return triples
```
# Strings
## License Key Formatting 
All we need to do with this question is firstly clean up the given string S by making it uppercase and replacing all instances of - with empty strings.
Now, the main trick to solving this problem is the fact that the first grouping can have any number of elements, hence this is why we need to work FROM THE END of the string. As all we really need to do is split the string into groups of size K, however the first group can be any size aslong as the rest are size K, meaning the first group is like the leftovers which we get from splitting the string into K units! Therefore, all we need to do to solve this problem is run a simple string splitting for loop, BUT FIRST REVERSE THE LIST, because we want to our leftovers which are not a full K units to be the first alphanumeric characters in the string. Finally, after completing the splitting process return the string reversed again, hence in the original order. 
```
def licenseKeyFormatting(self, S, K):
    S = S.replace('-','').upper()[::-1]
    #Replace the dashes, go uppercase, reverse the string
    new_S = []
    #Break the string into K units append each unit to new list
    for i in range(0, len(S), K):
        new_S.append(S[i:i+K])
    #Join the new list and return in after reversing! 
    return "-".join(new_S)[::-1]
```
## Next closest time
Remember the time conversions!
* 24 hour time to minutes is hours digit * 60 + minutes digits
* For this question you need to set each converted times digit individually, hence remember:
* Hours tens digit = total minutes / 60 / 10
* Hours ones digit = total minutes / 60 % 10
* Minutes tens digit = total minutes % 60 / 10
* Minutes ones digit = total minutes % 60 % 10
* Set up a hash set which contains all the values which you are allowed to work with
* Every times you increment you totalminutes check if that newly incremented value has digits which are all present in the hash set, if so flag will stay True we are done! return the result!
```
def nextClosestTime(time):
    hoursInMins = int(time[:2]) * 60
    totalMins = hoursInMins + int(time[3:])

    hashSet = set()
    for i in time:
        if i.isdigit():
            hashSet.add(int(i))

    while True:
        totalMins = (totalMins + 1) % (1440)
        totalNewTime = str(totalMins / 60 / 10) + str(totalMins / 60 % 10) + ":" + str(totalMins % 60 / 10) + str(
            totalMins % 60 % 10)

        flag = True
        for i in totalNewTime:
            if i.isdigit():
                if int(i) not in hashSet:
                    flag = False

        if flag == True:
            return totalNewTime
```
# Arrays
## Missing ranges
* Main idea is we think of lower and upper being included in the array
1. We set prev as lower - 1 as we do not want to include the given ranges in the output
2. Make sure the for loop range is len(nums) + 1 as we want to grab and use the upper range value in the last iteration
3. Every iteration compare the previous value + 1 with the current value - 1 this checks if there is indeed a valid range between the two elements
4. If this condition is true then we may only have one value between them so we call a helper function to do this check and return the correctly formatted result
5. Set previous to current each iteration as we increment current hence we can compare with each new element in the array, think of this as sliding a fixed size window across
```
def findMissingRanges(nums, lower, upper):
    ranges = []
    windowEnd = lower - 1
    for i in range(len(nums) + 1):
        windowStart = nums[i] if i < len(nums) else upper + 1
        if windowEnd + 1 <= windowStart - 1:
            ranges.append(formatStr(windowEnd + 1, windowStart - 1))
        windowEnd = windowStart
    return ranges
```
def formatStr(windowEnd, windowStart):
    return str(windowEnd) if windowEnd == windowStart else str(windowEnd) + "->" + str(windowStart)
# LinkedLists
## Merging K sorted linked lists
* Given a list which contains K linked lists to merge them into one sorted linked list the simplest idea seems to be to transfer all the elements in the list of linked lists into a single linked list
* The transfer all the elements of the single linked list into a simple array, sort the array, then make a new linked list add all the elements from the array in sorted order and voila!
* Time complexity o(n) as we need to iterate though the linked lists and auxillary space usage is o(n) to! So we can imporve there! 
```
def mergeKLists(lists):
    head = list2 = ListNode(0)
    for i in lists:
        current = i
        while current:
            list2.next = current
            current = current.next
            list2 = list2.next
    curr = head.next
    sortedArray = []
    while curr:
        sortedArray.append(curr.val)
        curr = curr.next
    sortedArray.sort()
    dummy = sortedLL = ListNode(0)
    for i in sortedArray:
        sortedLL.next = ListNode(i)
        sortedLL = sortedLL.next
    return dummy.next
 ```
## Remove nth node from end
* Dummy is the star here. By using dummy we are able to stay n + 1 behind runner, therefore we don't get any pesky edge case errors when current.next.next == None etc
* So main thing to remember is use dummy, stay n + 1 behind and always return dummy.next.
```
def removeNthFromEnd(head, n):
    dummy = current = ListNode(0, head)
    runner = head
    for i in range(n):
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next
    current.next = current.next.next
    return dummy.next
```
## Remove duplicates in linked list
* General idea here is to iterate through to linked lists and compare their elements we use nested while loops.
1. Set reference variables for each linked list object
2. Set a outer loop counter, a matched elements counter and a inner loop reset counter
3. Iterate any list with the outer loop counter < self.size()
4. Nested while loop with inner_loop_counter < other.size()
5. During this while loop check if the current data of the current linked list is equal to the one current data in the self linked list, if it is then add 1 to the counter, if not the increment the outer loop counter and do other = other.get_next()
6. Finally just check if the matched counter is == size of both linked lists
```
def remove_dupes(linked_list):
    current = linked_list.get_head()  # Current will point to head node of linked list
    runner = linked_list.get_head()  # Runner also points at head node of linked list
    while current != None:  # Iterate while current != None
        while runner.get_next() != None:  # While the element after the head element also does not equal None
            if current.get_data() == runner.get_next().get_data():  # If the current data in the linked list is present in the next node of the linked list
                runner.remove_after()  # Remove that node
            else:
                runner = runner.get_next()  # Else increment runner
        runner = current.get_next()  # Reset runner to the next element of the linked list
        current = current.get_next()  # Reset current to the next element of the linked list
```
# Sorting & Searching
# Stacks
## Valid parentheses
* Add only the open brackets to the stack
* If closed bracket then pop item at the top of the stack
* Check if they form a pair of valid brackets 
* If they do carry on else return False
* Finally if the len of the stack is 0 and the length of the string was greater than 1 we return True as all conditions met else False
```
def isValid(self, s):
    stack = []
    validBrackets = ["[]", "{}", "()"]
    openBracket = ["(", "[", "{"]
    for i in s:
        if i in openBracket:
            stack.append(i)
        elif len(stack) > 0:
            bracket = stack.pop()
            if bracket + i in validBrackets:
                pass
            else:
                return False
        else:
            return False
    return True if len(s) > 1 and len(stack) == 0 else False
```
# Queues
# Priority Queues/Heaps
# Trees
# Hash tables
# Dynamic Programming 
## Kadane's Algorithm - Maximum Subarray
The way to approach the maximum Subarray problem is by using Kadane's algorithm. How Kadane's algorithm works is, we start off with the first index element in the array. We set our current max and global max to this element. We then want to iterate through the remainder of the array, we want to build up the sum in our current max variable. However, what we are going to do is always take the maximum between the current array elemet (list[i]) and the current array element plus whatever we have in our current sub array so (list[i] + current_max). This was we only take the maximum sub array in each iteration, this is how we build up our current maximum sub array. Then each iteration, we ask is the current sum of our current_max subarray LARGER than the sum in the global_max subarray? We the update accordingly. Finally we are left with the largest subarray sum in global_max. 
```
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
```
## Jump Game
*  We use a greedy backtracking approach. It is quite simple.
*  Given [2, 3, 1, 1, 4] all we want to do is start from the last index element in the array, hence the target.
*  We are just going to go backwards and check if we are able to reach the previous element, hence the element we just came from.
*  This means that if we can get to the 0th index from the end we are able to reach the last element in the list, else we are not.
*  ie [2, 3, 1, 1, 4], start at 4, i + nums[i] = 4 + 4 > lastgoodindex = 4 is reachable, therefore move down the list, update lastgoodindex to be i
*  Now i moves to 3. i + nums[i] = 3 + nums[3] = 3 + 1 >= lastgoodindex = 3 is reachable, therefore move down and make lastgoodindex the next element so i = 2
*  i moves to 2. i + nums[i] = 2 + nums[2] = 2 + 1 >= lastgoodindex = 2 is reachable, therefore move down and make lastgoodindex the next element so i = 1
*  i moves to 1. i + nums[i] = 1 + nums[1] = 1 + 3 >= lastgoodindex = 1 is reachable, update lastgoodindex to i = 0
* i moves to 0. i + nums[i] = 0 + nums[0] = 0 + 2 >= lastgoodindex = 0 is reachable. We are done. 
```
def canJump(nums):
    lastGoodIndex = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= lastGoodIndex:
            lastGoodIndex = i
    return True if lastGoodIndex == 0 else False
```        
## Maximum distance to closest person
* Idea is to make a copy array which contains all 0's and same len as given array. Do passes from the left and from the right of the given array. Record in the copy array at the exact same index of the given array the distance since last seen 1.
* We take the minimum from distance and lastseen[i] because we are looking both ways. hence the min last seen 1 maybe closer to the right than the left and vice versa
* We have the conditional statement lastSeen[i] == 0 to account for 0's in the beginning or end of the array
* Returning the max element in the list return the index of the element which was furtherest from 1's given both left and right passes
* Note this is O(n) time and O(n) auxillary space. We can do this in O(1) space!
```
def maxDistToClosest(seats):
    lastSeen = [0] * len(seats)
    distance = -1
    for i in range(len(seats)):
        if seats[i] == 0 and distance != -1:
            distance += 1
            lastSeen[i] = distance
        else:
            distance = 0

    distance = -1
    for i in range(len(seats) - 1, -1, -1):
        if seats[i] == 0 and distance != -1:
            distance += 1
            if lastSeen[i] == 0:
                lastSeen[i] = distance
            else:
                lastSeen[i] = min(distance, lastSeen[i])
        else:
            distance = 0
    return max(lastSeen)
```    
## Trapping rainwater
* Idea is the list in question "height" depcits the possible water levels at each specific index.
* What we are going to do is find the height of the each "building" at each index in the given "height" array
* How we do this is we make to dp (dynamic programming) lists, we parse left and append only the max values of each consecutive index to the list
* We parse right and append the max element values for all indexes to the dpRight list. NOTE WITH DPRIGHT WE MUST REVERSE THE LIST
* Finally we are going to take the min of the correpsonding values in both of these lists and store that in either or dpLeft or dpRight list, does not really matter
* BUT the main idea will be we must deduct the corresponding height indexes to! Recall the height list depicts the possible water level.
* It all comes together here! So the min of dpLeft and dpRight will give us the index of the buildings, the corresponidng height index gives us the value of possible water evels at each corresponding index.
* Hence, if we deduct the building height from the possible water level we get the water level for that specific index.
* Therefore, dpLeft will be left with just the total possible water levels from each given index from the list in question, so just return the sum of its values for the total water level. Done! 
```
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
```
