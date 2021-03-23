# DSA and Leetcode walkthroughs 
This project contains comprehensive walkthroughs for how to solve data structures and algorithm related problems. I detail how I derived my solution, algorithms, and how to build intuition and discover patterns to solve these problems efficiently.

# Topological Sort
![1](https://user-images.githubusercontent.com/57751792/110879693-4bef8280-8342-11eb-9f53-09fdae5e5df6.jpg)
![1](https://user-images.githubusercontent.com/57751792/110879708-501ba000-8342-11eb-9a5c-5ea13d3f4260.png)
## Course Schedule II - Topological Sort & DFS Application
* We have n courses which means we have n nodes in our graph. 
* If we have a cycle we return [] as we have an impossible ordering of courses. ie [[1, 0], [0, 1]].
* This ordering means to take course 1 we need to take course 0 and to take course 0 we need to take course 1, hence impossible, hence cycle.
* Also watchout for edgecases such as empty list.
* We will use Topological sort and DFS.
1. Build an adjacency map, this will hold each prereq and its "children" hence the courses which are available after taking this prereq.
2. Build of DFS recursive function to visit the nodes in the graph 
3. Make a output list to add the topological order of the courses and two sets which contain the visited nodes and check for cycles
```
def findOrder(self, numCourses, prerequisites):
    prereq = {i:[] for i in range(numCourses)}
    for course, prereqs in prerequisites:
        prereq[course].append(prereqs)

    output = []
    visit, cycle = set(), set()

    def dfs(courses):
        if courses in cycle:
            return False
        if courses in visit:
            return True

        cycle.add(courses)
        for i in prereq[courses]:
            if dfs(i) == False: return False
        cycle.remove(courses)
        visit.add(courses)
        output.append(courses)
        return True

    for i in range(numCourses):
        if dfs(i) == False:
            return []
    return output
```
# Sliding Window Patterns
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
## Building trees from preorder, inorder and postorder traversal lists
The pattern here is that we always use the inorder traversal list to build the tree. In particular, we can dervie the root indexes easily from both preorder and postorder as preorder root = 0th element and postorder root = -1 element in respective lists. Now we know that once we have the main root we can identify the left and right subtrees from the inorder list. We then recursively keep popping off the indexes and assigning them as roots from the pre/postorder traversal lists, building left subtree to right subtree recursivley for preorder and right subtree to left subtree recursivley for postorder. 
```
def buildTree(inorder, postorder):
    def recurse(inorder, postorder):
        if not inorder or not postorder: return
        root = TreeNode(postorder.pop())
        root.right = recurse(inorder[inorder.index(root.val) + 1:], postorder)
        root.left = recurse(inorder[:inorder.index(root.val)], postorder)
        return root

    return recurse(inorder, postorder)
```
```
def buildTree(preorder, inorder):
    def recurse(preorder, inorder):
        if not inorder: return
        root = TreeNode(preorder.pop(0))
        mid = inorder.index(root.val)
        root.left = recurse(preorder, inorder[:mid])
        root.right = recurse(preorder, inorder[mid + 1:])
        return root
    return recurse(preorder, inorder)
```

However, we can optimize this by using a hash table and "binary search" pattern. All we do is assign the inorder indexes and corresponding values to the hash table, hence we get O(1) searching/indexing time for finding the mid, and instead of the lists, we pass to min and max indexes which we increment in respect to mid, so similar to a binary search.
*OPTIMAL
```
def buildTree(preorder, inorder):
    hashMap = {value: index for index, value in enumerate(inorder)}
    def recurse(minVal, maxVal):
        if minVal > maxVal: return
        root = TreeNode(preorder.pop(0))
        mid = hashMap[root.val]
        root.left = recurse(minVal, mid - 1)
        root.right = recurse(mid + 1, maxVal)
        return root
    return recurse(0, len(inorder) - 1)  # (36 ms, faster than 99.21%, 18.1 MB, less than 90.83%)
```
```def buildTree(inorder, postorder):
    hashMap = {inorder[i]: i for i in range(len(inorder))}
    def recurse(minVal, maxVal):
        if minVal > maxVal: return
        root = TreeNode(postorder.pop())
        midVal = hashMap[root.val]
        root.right = recurse(midVal + 1, maxVal)
        root.left = recurse(minVal, midVal - 1)
        return root
    return recurse(0, len(inorder) - 1)
```
# Recursion
# Backtracking pattern 
## 1. What is backtracking? 
* Choice, constraint, goal. 
* Choice = What do you want to do at X? ie if using backtracking to solve a sudoku puzzle, what do you want to do at each cell is your "Choice". Choice also = "Decision space".
* Constraints = Restrictions of decision space. ie only values between 2-9.
* Goal = What is the end goal? What are we trying to accompolish? How can we break down this problem into pieces and recusivley solve this with backtracking?
## 2. Backtracking example:
```
def letterCombinations(self, digits):
    if digits == "":
        return []
    hash_map = {1: [], 2: ["a", "b", "c"], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
    def backTrack(path, index):
        if index == len(digits):
            combinations.append("".join(path))
            return
        else:
            curr_key_letters = hash_map[int(digits[index])]
            for letter in curr_key_letters:
                path.append(letter)
                backTrack(path, index + 1)
                path.pop()

    combinations, path = [], []
    backTrack(path, 0)
    return combinations
```
## Explanation:
* What is happening here is that we are given a graph, each node in the graph has 3 or 4 children which are alphabet letters and the node value itself is a numerical digit.
* We need to find all possible combinations given X digits. For example, given digits = "23" we would have [ad, ae, af, bd, be, bf, cd, ce, cf]. Now I want you to notice something very important here. The fact that I said "ALL POSSIBLE COMBINATIONS" should make you think of recursion and backtracking.
* So how do we do this? 
* We need to follow backtracking methodology!
* Make a choice: What do you want to do at each letter? We want to take each 0th index digit in the digits string and add to it all of the 1th index digits string letters.
* What are the constraints? Not many! Just don't repeat any strings.
* What is the goal? The sub goal at each level is to attain a string which has the same length as digits and is a combination of digits[0] letter and digits[1] letter.
## Lets walk through the code:
* The most important part of the code is the for loop, what is happening is we intially start with looking at the 0th digit letters in the hash map, this is going to be our "upper level" for loop, we append the initial letter to our constructor list, we then recurse, we move on to digits[1] letters in the hash map, now we rebegin our for loop but this time our letters are the 1th index letters of digits, ie if digits = 23, then upper level for loop = 2 = [a, b, c] and recursive level for loop = 3 = [d, e, f]. Then we add our current recurisve level letter to our consturctor list which already contains the first letter of digits[0]. Now we would have [a,d] for example. Awesome, we have our first string, we have solved one of the sub problems. Now we recurse again passing index + 1 which is 2 which means we hit our base case, hence we have one of the requried strings for the out put so we can add it to the final list then return to the previous call. Now the previous call was made by index + 1, so we return there. Now that we have retured to this call we backtrack, we pop off the current letter from consturct list, which would leave us with [a], and move onto the next letter in the for loop! So now we are at e. Once we have visited all the letters for digits[1] we return to digits[0] which will pop off the current element and repeat the exact same backtracking process with the next letter.
## Letter combinations of a phone number - Backtracking
 1. So we are given from 0 to 4 possible digits and we need to find all possible letter combinations for these digits.
 * ie: "23" = 2 = [a, b, c] and b = [d, e ,f] hence 23 = [ad, ae, af, bd, be, bf, cd, ce, cf]
 2. Do some error checking in case of empty strings.
 3. Build the hash map which has keys as the numbers and values as their respective letters
 4. We then make our recursive function where we will do the meat of the work.
 5. We use backtracking. We make all possible combinations with the 0th index digit key. When we hit an index equal to digits, we have made a valid combination, hence we return pop off the current element and restart the backtracking process.
 6. Time complexity is O(x^n) * O(n), with X^n being X digits passes and n possibilities per digit. The O(n) because we need to visit O(n) elements.
 7. Space complexity is O(n) as we build our call stack. 
```
def letterCombinations(self, digits):
    if digits == "":
        return []
    
    # Mapping where each key is the digit number and values are the letters assigned to it.
    hash_map = {1: [], 2: ["a", "b", "c"], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
    
    # Recursive function to generate the combination strings.
    def backTrack(path, index):
        if index == len(digits):
            combinations.append("".join(path))
            return
        else:
            curr_key_letters = hash_map[int(digits[index])]
            for letter in curr_key_letters:
                path.append(letter)
                backTrack(path, index + 1)
                path.pop()

    combinations, path = [], []
    backTrack(path, 0)
    return combinations
```
## Generate parenthesis
![1](https://user-images.githubusercontent.com/57751792/111856575-8a172280-8990-11eb-9331-b5112a9b39f0.png)
![1](https://user-images.githubusercontent.com/57751792/111856577-8b484f80-8990-11eb-8407-3e60794ff5fe.png)
 1. We use backtracking. Choice, constraints, goal.
 2. Choice = Will we place a open ( or closed ) bracket?
 3. Constraints:
 * Can only place open if open < n, ie if n = 3 then we have at max ((( ))) of each bracket. Therefore if open = 4 we would have (((( thus invalid.
 * Close < open in order to place close. If close == open then we could place )( which is invalid. If close > open then ))( hence invalid.
 * Max size of the string is 2 * n, why? Because if n = 3 we can have 3 open brackets (((, and 3 closing bracket ))) at max hence 6 in total.
 4. Goal = find all possible valid combinations, if we stick to our constraints then we WILL get all valid options.
 5. Rest is simple, we basically just backtrack, nearly exact same story as letter combinations of a phone number, just rememeber we must pop off the recently added element from the stack for backtracking!
 6. Also, of course iteration starts at 0, 0 for open and closed as we haven't placed any brackets yet.
```
def generateParenthesis(self, n):
    result, stack = [], []

    def backTrack(open_count, close_count):
        if len(stack) == (2 * n):
            result.append("".join(stack))
            return
        if open_count < n:
            stack.append("(")
            backTrack(open_count + 1, close_count)
            stack.pop()
        if close_count < open_count:
            stack.append(")")
            backTrack(open_count, close_count + 1)
            stack.pop()

    backTrack(0, 0)
    return result
```
## Fibbonacci with and without memoization
## Fibbonacci(n) = Fibbonacci(n-1) + Fibbonacci(n-2)
* Basic fibbonacci sequence recursive function
```
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(6))
```
* Fibbonacci sequence with memoization
```
def fibM(n, memo={}):
    if n in memo:
        return memo[n]
    elif n < 2:
        return n
    else:
        memo[n] = fibM(n-1) + fibM(n-2)
        return fibM(n-1) + fibM(n-2)
```
# Math
## Gaussian summation: n(n + 1)//2
* Gaussian summation formula = n(n + 1)/2 this will give us the sum of all the natural numbers from 0 to n. Beautiful formula.
```
def missingNumber(self, nums):
    # Remember the Gaussian summation formula! The sum of a sequence is n(n+1)/2
    # This is a beautiful solution. The sum as the gauss formula gives us the sum of n natural numbers and we use that sum to figure out which value is missing as the sum of the nums array is going to give us the sum of n natural numbers also, minus one number from that set of n naturals, and we can easily find that number by taking the difference between the guassian and array sum.
    gauss = len(nums) * (len(nums) + 1) // 2
    num_sum = sum(nums)
    return gauss - num_sum
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
def formatStr(windowEnd, windowStart):
    return str(windowEnd) if windowEnd == windowStart else str(windowEnd) + "->" + str(windowStart)
```
## Best time to buy and sell stocks (One day only)
1. Don't make the mistake of looking for the MAX value to sell at and focusing entirely on that! The key here is the min_val.
2. Why min val? Because what's the point in finding the highest price to sell at if you already have a really high buy price?
3. You should look for BOTH the lowest price to buy at and highest price to sell at!
4. That's why the min_val update is there, because if our current value is cheaper than our previous value which we bought at we should update! And take that discounted price!
5. Keep this in mind! For these stock problems don't always go for the max price to sell consider both!
6. Time complexity is O(n), space complexity is O(1).
```
public class BestTimeToBuySellStock {
    public int maxProfit(int[] prices) {
        int min_val = prices[0];
        int max_profit = 0;
        for (int i = 1; i < prices.length; i++) {
            max_profit = Math.max(max_profit, prices[i] - min_val);
            min_val = Math.min(min_val, prices[i]);
        }
        return max_profit;
    }
}
```
## Best time to buy and sell stocks (multiple days)
* Look idea is super straight forward! I want to buy every day and sell every day BUT if I sell for a loss just add 0! It's a glitch in the system lol. 
```
public class BestTimeToBuySellMultiple {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            max_profit += Math.max(prices[i + 1] - prices[i], 0);
        }
        return max_profit;

    }
}
```
## Maximum subarray
```
public class MaximumSubArray {
        public int maxSubArray(int[] nums) {
        int currMax = nums[0]; int globalMax = nums[0];
        for (int i = 1; i < nums.length; i++) {
            currMax = Math.max(nums[i], nums[i] + currMax);
            globalMax = Math.max(globalMax, currMax);
        }
        return globalMax;
    }
}
```
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
## Copy list with random pointer 
* We make a hash table and simply do two passes through our given linked list in question.
* First pass we make the key of the hash table equal to the reference in memory of each respective node in the linked list and the value in the hash table will be a NEW node element which has the same VALUE as the current node we are looking at.
* So now we have a hash table which contains values which are nodes with no connections to any other nodes, they are just sitting there waiting to be connected up. We also have keys which are the memory references which allow us to index in with O(1) time.
* We now do our second pass, we are now going the make the connections for the copied nodes in the hash table.
* We set the next node of the copied node "hashMap[current].next" as the next node of the corresponding key in the hash table, meaning the next node of the original node in the linked list.
* We set the random node for the copied node "hashMap[random].next" as the random node for the original node in the original linked list.
* Make sure to check that the nodes do not equal none for random or next.
* Finally we return the hashMap values which are going to be connected now as a linked list from the head value. 
```
def copyRandomList(head):
    if not head: return None
    current = head
    hashMap = {}

    while current:
        hashMap[current] = Node(current.val, None, None)
        current = current.next

    current = head
    while current:
        if current.next:
            hashMap[current].next = hashMap[current.next]
        if current.random:
            hashMap[current].random = hashMap[current.random]
        current = current.next
    return hashMap[head]
```
## Majority Element in Array
```
class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}
```
# Sorting & Searching
## Binary Search: O(log n), cuts the problem size in half each iteration.
```
def binarySearch(sorted_array, element_to_find):
    min_index = 0
    max_index = len(sorted_array) - 1
    while min_index <= max_index:
        mid = (min_index + max_index) // 2
        if sorted_array[mid] == element_to_find:
            return mid
        elif sorted_array[mid] < element_to_find:
            min_index = mid + 1
        elif sorted_array[mid] > element_to_find:
            max_index = mid - 1
    return -1
```
## Recursive implementation of binary search. O(log n) runtime as problem is cut in half but uses extra space for recursive call stack.
```
def recursiveBS(min_index, max_index, element_to_find, array):
    index = 0
    if min_index > max_index:
        return -1
    else:
        mid = (min_index + max_index) // 2
        if array[mid] == element_to_find:
            index = mid
            return index
        elif array[mid] < element_to_find:
            index = recursiveBS(mid + 1, max_index, element_to_find, array)
        elif array[mid] > element_to_find:
            index = recursiveBS(min_index, mid - 1, element_to_find, array)
    return index


def findIndex(array, element_to_find):
    return recursiveBS(0, len(array)-1, element_to_find, array)
```
## Trinary search
```
def trinary_search(my_list, x):
    min = 0
    max = len(my_list) - 1
    mid_points_computed = []
    while min <= max:
        mid1 = min + (max - min) // 3
        mid2 = max - (max - min) // 3
        mid_points_computed.append(mid1)
        if x > my_list[mid1]:
            mid_points_computed.append(mid2)
        if my_list[mid1] == x:
            return (mid1,mid_points_computed)
        elif my_list[mid1] < x:
            if my_list[mid2] == x:
                return (mid2,mid_points_computed)
            elif my_list[mid2] > x:
                min = mid1 + 1
                max = mid2 - 1
            elif my_list[mid2] < x:
                min = mid2 + 1
        else:
            max = mid1 - 1
    return (-1,mid_points_computed)
```
## Bubble Sort 
* Bubble sort sorting algorithm works by comparing the element at the current index with the element adjacent to it, hence its direct neighbour.
* If the element which is adjacent is less than the current element, it will swap both elements. This repeats for every single element in the array.
* Therefore, we call it bubble sort because the largest element in each iteration will bubble up to the top of the array.
* We can also note that bubble sort would do the most work on an reverse sorted array such as [7,6,5,4,3,2,1] as it will have to swap every element.
* Important to note that you should have a break statement in case there are no swaps conducted in the inner loop which indicates that the array is now in sorted order, hence, we can return.
* Bubble sort time complexity is O(n^2)
* Bubble sort space complexity is O(1), hence constant auxiliary space usage as everything is indeed happening in place.
```
def bubbleSort(array):
    for i in range(1, len(array)):
        swap = False
        for n in range(len(array) - 1):
            if array[n] > array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]
                swap = True
        if swap == False:
            break
    return array
print(bubbleSort([7, 6, 5, 4, 3, 2, 1]))
```
## Insertion sort
* Insertion sort works by partitioning the array into sorted and unsorted sections.
* Insertion sort will assume the first index in the array is already in sorted order.
* It will be compare the last element in the sorted section with the first unsorted element in the array.
* If the first unsorted element is less than the last sorted element it will swap these two elements, It will then continue to check the unsorted element with all of the elements in the sorted section.
* Once it find a element in the sorted section less than the unsorted element or it hits the 0th index the while loop will break and we place the element there, thus adding it to our sorted section.
* What makes insertion sort useful is the fact that you can add whatever conditions you want to sort the array by, ie you can sort by length, by last letter, literally anything you want and it's quite simple! All you need to d ois specify it in the while loop condition.
* Insertion sort time complexity is O(n^2) and space complexity is O(1) so everything is happening in place.
```
def insertionSort(array):
    for index in range(1, len(array)):
        value = array[index]
        i = index - 1
        while i >= 0 and array[i] > value: # Change the condition here in order to sort in respect to a different parameter.
            array[i + 1] = array[i]
            array[i] = value
            i -= 1
    return array

print(insertionSort([7,6,5,4,3,2,1]))

def ReverseinsertionSort(array):
    for index in range(1, len(array)):
        value = array[index]
        i = index - 1
        while i >= 0 and array[i] < value: # Reverse sort
            array[i + 1] = array[i]
            array[i] = value
            i -= 1
    return array

print(ReverseinsertionSort([7,6,5,4,3,2,1]))


def LengthinsertionSort(array):
    for index in range(1, len(array)):
        value = array[index]
        i = index - 1
        while i >= 0 and len(array[i]) > len(value): # Length sort string array.
            array[i + 1] = array[i]
            array[i] = value
            i -= 1
    return array

print(LengthinsertionSort(["goku", "vegeta", "gohan", "frieza", "Perfect cell"]))
```
## Selection sort
* There are two ways to implement selection sort, one is if we sort from top down or bottom down. Both ways have the same principle so your fine with doing it either way, i prefer top down.
* Selection sort will begin iteration from the end of the array, in each iteration it will find the largest element in the unsorted section (which is the entire array at iteration 0)/
* It will swap the largest unsorted element with the first element in the unsorted section of the array which begins at the very end of the array.
* Hence, you can imagine that in each iteration we are building the array from the top down.
* Selection sort time complexity is O(n^2) and auxiliary space usage is O(1), so at least it's nice the it uses constant space.
```
# Top down, main idea is we go from the end of the list and swap the largest elements
def selectionSort(array):
    for i in range(len(array)-1, -1, -1):
        largest = 0
        for n in range(i + 1):
            if array[n] > array[largest]:
                largest = n
        array[i], array[largest] = array[largest], array[i]
    return array

print(selectionSort([7,6,5,4,3,2,1]))

# Bottom up, main idea is we go from the front of the list and swap the smallest elements
def selectionSortBU(array):
    for i in range(0, len(array)-1):
        smallest = i
        for n in range(i + 1, len(array)):
            if array[n] < array[smallest]:
                smallest = n
        array[i], array[smallest] = array[smallest], array[i]
    return array

print(selectionSortBU([7,6,5,4,3,2,1]))
```
## Bogosort
```
import random
def bogosort(list_of_elements):
    n = len(list_of_elements)
    while is_sorted(list_of_elements) == False:
        shuffle(list_of_elements)

def is_sorted(list_of_elements):
    n = len(list_of_elements)
    for i in range(0, n - 1):
        if list_of_elements[i] > list_of_elements[i + 1]:
            return False
    return True

def shuffle(list_of_elements):
    n = len(list_of_elements)
    for i in range(0, n):
        random_index = random.randrange(0, n - 1)
        list_of_elements[i], list_of_elements[random_index] = list_of_elements[random_index], list_of_elements[i]

my_list = [1, 3, 4, 2]
bogosort(my_list)
print(my_list)
```
## Mergesort
```
def mergesort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2  # Finding the mid of the array
        left_sublist = a_list[:mid]  # Dividing the array elements
        right_sublist = a_list[mid:]  # into 2 halves
        mergesort(left_sublist)  # Sorting the first half
        mergesort(right_sublist)  # Sorting the second half
        small_unsort_left = small_unsort_right = main_list_pos = 0

# Copy data to temp arrays L[] and R[]
        while small_unsort_left < len(left_sublist) and small_unsort_right < len(right_sublist):
            if left_sublist[small_unsort_left] < right_sublist[small_unsort_right]:
                a_list[main_list_pos] = left_sublist[small_unsort_left]
                small_unsort_left += 1
            else:
                a_list[main_list_pos] = right_sublist[small_unsort_right]
                small_unsort_right += 1
            main_list_pos += 1

    # Checking if any element was left
        while small_unsort_left < len(left_sublist):
            a_list[main_list_pos] = left_sublist[small_unsort_left]
            small_unsort_left += 1
            main_list_pos += 1
        while small_unsort_right < len(right_sublist):
            a_list[main_list_pos] = right_sublist[small_unsort_right]
            small_unsort_right += 1
            main_list_pos += 1
    return a_list

print(mergesort([8, 7, 6, 5, 4, 3, 2, 1]))
```
## Quicksort
```
def quick_sort(a_list):
    if len(a_list) < 2:
        return a_list
    else:
        pivot = a_list[0]
        less = quick_sort([i for i in a_list if i < pivot])
        greater = quick_sort([i for i in a_list if i > pivot])
        return less + [pivot] + greater

print(quick_sort([7,6,3,99]))
```
## Find the median in an array
```
def findMedianSortedArrays(nums1, nums2):
    new_nums = []
    # Edge cases
    if len(nums1) == 0 and len(nums2) == 0:
        return []
    elif len(nums1) == 0 and len(nums2) != 0:
        new_nums = nums2
    elif len(nums2) == 0 and len(nums1) != 0:
        new_nums = nums1
    else:
        new_nums = nums1 + nums2

    if len(new_nums) == 1:
        return float(new_nums[0])
    new_nums.sort()
    mid = (0 + len(new_nums) - 1) // 2
    if len(new_nums) % 2 != 0:
        return new_nums[mid]
    else:
        return (new_nums[mid + 1] + new_nums[mid]) / 2.0
```
## Quartile elements in an array
* We want to print the values in the upper and lower quartile of our list
* The lower quartile is the value which is 25% larger than all other values in the list
* The upper quartile value is the value for which 75% of the list elements are smaller than
* This is a simple process all we require is to give the value which is at the 25% and 75% indexes
of the list.
```
def get_quartiles(list_of_numbers):
    list_of_numbers.sort()
    #We must sort the list!
    lower_quartile = int(len(list_of_numbers) * 0.25)
    #Simply take the lenth of the list and mutliply it by 0.25
    #The length of the list in a percentage is 100% and we want 25% from this 100%
    #Therefore when we multiply the length of the list by 0.25 we derive the value which
    #is equivalent to 25% of the length of the list
    upper_quartile = int(len(list_of_numbers) * 0.75)
    #We want the 75% index value of the list. Therefore we mutiply by 0.75 which gives us
    #the 75% index out of the 100% index of the list
    median_quartile = int(len(list_of_numbers) * 0.5)
    #This will give us the index right in the middle of the list
    return list_of_numbers[lower_quartile], list_of_numbers[upper_quartile]
```
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
## Decode string
1. Idea is we use a stack, where each element in the stack is a list, the list contains the current string and current repeat value, we know it is the current string because we have not yet hit a closed bracket because once we hit the closed bracket we pop off.
2. Initialize a stack which contains an empty string and int 1. This is just our final element in the stack which we need to return.
3. Iterate through the string, we do k * 10 + int(i) because in this would be the best way to get values numerical values greater than 1 digit.
4. Next we see if we have a open bracket, if we do that means we start a new list and we will build the string in this list until we hit a closing bracket, we also add the k value, remember to reset the k value at this step also for each new list.
5. Finally, if we hit a closing bracket we assign two variables, one wil hold the string the other will hold the numerical value we will then mutliply that string and add it to our previous stack list element, this is how we continously build our string but adding the previous lists strings in the stack.
6. If we have simple character then just add it onto the current string portion of the list at the top of the stack.
7. Return the string portion of the last element in the stack which will hold the decoded list.
```
def decodeString(self, s):
    stack = [["", 1]]
    k = 0
    for i in s:
        if i.isdigit():
            k = k * 10 + int(i)
        elif i == '[':
            stack.append(["", k])
            k = 0
        elif i == ']':
            char_string, repeat_val = stack.pop()
            stack[-1][0] += char_string * repeat_val
        else:
            stack[-1][0] += i
    return stack[-1][0]
```
# Queues
# Priority Queues/Heaps
# Trees
## BFS = Breadth First Search = Level Order Traversals = Queues
## DFS = Depth First Search = Preorder, Inorder, Postorder Traversals = Stacks
## BFS Binary Tree
1. Check if the root is empty, hence if the tree is empty.
2. We are going to use queues to solve this problem as the queue FIFO property works well here.
3. Initialize a queue to hold the current root node
4. level is going to be an empty list/queue which we use to add in all the nodes at the particular level in the tree
5. next queue is going to hold the nodes in the NEXT level of the binary tree
6. result will store our nested list representation of the level order of the tree
* The main idea is that starting off with the root, we loop thorugh all the nodes level by level, we add the nodes at each respective level to the level queue and we add their children to the next queue
* After the end of each loop we transfer the nodes at the respective level into our results queue, we now want to look at the next level in the tree, hence we assign our queue to point to the next_queue variable which holds the next level nodes.
* We empty the next_queue variable and level queues and repeat this same process until there are no more nodes left to visit.
```
 Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def levelOrder(root):
    if not root: return []
    queue = [root]
    level = []
    next_queue = []
    result = []
    while queue:
        for root in queue:
            level.append(root.val)
            if root.left:
                next_queue.append(root.left)
            if root.right:
                next_queue.append(root.right)
        result.append(level)
        queue = next_queue
        next_queue = []
        level = []
    return result
```
## DFS Preorder Recursive & Iterative
* Recursive solution
```
# Preorder = print, left, right. DFS = moving down the tree. 
def preorderTraversal(self, root):
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root != None else []
```
* Iterative solution
* We use stacks for the iterative implementation of preorder
* The idea is, set up the stack to initially hold the root node, then while the stack is not empty, follow the preorder protocol of node, left, right.
* One thing to be very mindful of here is that we are doing everything in the OPPOSITE order of the traversal, as recall stacks have the LIFO property. ie a good example is to think of it has preorder = [node, left, right] then when using a stack we would have [right, left, node] as we WANT the node value first.
* Pop the value at the top of the stack and append it to the results list, then append the correpsonding left and right children.
* We keep repeating this process and derive the preorder traversal of the tree.
```
def preorderTraversal(self, root):
    if not root: return []
    stack = [root]
    result = []
    while stack:
        root = stack.pop()
        result.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return result
```
## DFS Inorder recursive and iterative
* Recursive solution
* Inorder = left, print, right. DFS = Moving down the binary tree, depth of the tree.
```
def inorderTraversal(self, root):
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root != None else []
```
* Iterative solution
* Main idea is our main loop iterates while root or stack are both not empty/null.
* The inner while loop is used to traverse to the left as far as possible. It build up our stack, and once we hit the leaf with no left child we break out of this loop
* Once we break out of the left iterative loop, we pop off the last element pushed onto the stack, so the last left node with no left child, we append this value to our results list
* We then want to iterate right and visit the right subtree of the same node. When we iterate right once, our inner left loop will rebegin and complete the process again of finding the leftmost node
* Notice the pattern here! Inorder is left, node, right. We have two while loops, we begin by always going as far left as possible, when that break we add our node at the top of the stack, then we go right. Make sense yea.
```
def inorderTraversal(self, root):
    stack, result = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result
```
## DFS Postorder recursive and iterative 
* Recursive solution
* Postorder = left, right, print. 
```
def postorderTraversal(root):
    return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []
```
## Memoization - Longest increasing path in matrix 
1. Idea is we have a matrix and we want to find the longest increasing path in the matrix.
2. Approach this matrix as a directed graph. Each element of the matrix is a vertice.
3. The basic approach is simple. Take each individual element in the matrix and do a DFS search through the entire matrix with conditions that require the next value in the path to always be greater than the current.
4. As long as this recursion keeps going, we are adding to the path for the one specific element, at the end we just return the element with the maximum path in the matrix.
5. However, we MUST alter this algorithm to a degree as it is to expensive! We will use Memoization to make this algorithm more efficient. Check out this piece on Memoization below.
![1](https://user-images.githubusercontent.com/57751792/111094053-3e830400-859f-11eb-9b64-9db1387626c1.jpg)
* Now if we use memoization the algorithm will be as follows.
1. Define a final variable DIRECTIONS which holds down, up, left, right indexes respectively. We will use with our DFS to build our path.
2. Define a memoization matrix which has dimensions m x n and is populated with all 0's. We will use this matrix, in particular, each element in this matrix will correspond to each element in the original matrix.
3. The way the memoization matrix and OG matrix correlate is that once we have done a DFS search throughout our entire matrix for any one element, we will set the value of the element at its corresponding index in the memoization matrix as the value of the maximum increasing path for that OG matrix element.
4. Therefore, we don't have to recompute the path every single time! We can simply do a check and see, hey is this 0? if it is then I haven't calculated it's path yet, if it isn't then I need to find the max path for this element, so I will go ahead and DFS.
5. At the end of that DFS i set that element to the maximum path it could have taken + 1 to account for it's own path as each element itself is counted as a valid path.
```
public class LongestIncreasingPathMatrix {

    private int[][] DIRECTIONS = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix.length == 0 || matrix == null) return 0;
        int rows = matrix.length;
        int cols = matrix[0].length;
        int longestPath = 0;
        int[][] memoization = new int[rows][cols];
        for (int currRow = 0; currRow < rows; currRow++) {
            for (int currCol = 0; currCol < cols; currCol++) {
                int longest = dfs(matrix, memoization, rows, cols, currRow, currCol);
                longestPath = Math.max(longestPath, longest);
            }
        }
        return longestPath;
    }

    public int dfs(int[][] matrix, int[][] memoization, int rows, int cols, int currRow, int currCol) {
        if (memoization[currRow][currCol] != 0) return memoization[currRow][currCol];
        int max = 0;
        for (int[] direction : DIRECTIONS) {
            int X = direction[0] + currRow;
            int Y = direction[1] + currCol;
            if (X >= 0 && Y >= 0 && X < rows && Y < cols && matrix[X][Y] > matrix[currRow][currCol]) {
                int longest = dfs(matrix, memoization, rows, cols, X, Y);
                max = Math.max(max, longest);
            }
        }
        memoization[currRow][currCol] = max + 1;
        return memoization[currRow][currCol];
    }
}
```
## Evaluate division
![1](https://user-images.githubusercontent.com/57751792/111568715-19dc9580-8806-11eb-90b8-91b5015d5008.jpg)
![1](https://user-images.githubusercontent.com/57751792/111568648-fca7c700-8805-11eb-8471-88e31c82cb64.png)
```
def calcEquation(self, equations, values, queries):
    # Step 1: Build the graph
    graph = collections.defaultdict(dict)
    # Default dict beacuse if a value DNE it won't throw an expection unlike normal dict
    for (num, denom), product in zip(equations, values):
        # zip(equations, values) = [([a, b], 2.0), ([b, c], 3.0)]
        graph[num][denom] = product
        ## dict[x][y] implies x is pointing to y. ie {'a': {'b': 2.0}} a is pointing to b.
        # Set the key as the num, denom and value as the product of the division in the defaultdict
        graph[denom][num] = 1.0/product

    def dfs(numerator, denominator, visited):
        if numerator not in graph or denominator not in graph: 
            return -1.0

        if denominator in graph[numerator]:
            return graph[numerator][denominator]
        # Recall that our dict is set up such that the numerator points to the deominator, hence if denominator is in the denominator it 
        # is a key of the numerator so we can return that value.
        # ie {'a': {'b': 2.0}}, a is the numerator and b is the denominator. If the query was a/b we would ask "is b in a?" we can see it is hence we just return the value which is the product of a/b.

        for i in graph[numerator]:
            if i not in visited:
                visited.add(i)
                temp = dfs(i, denominator, visited)
                if temp == -1:
                    continue
                else:
                    return graph[numerator][i] * temp
        return -1
    result_list = []
    for numerator, denominator in queries:
        result_list.append(dfs(numerator, denominator, set()))
        # Pass the numerator and denominator of the query division to dfs where we will find the product.
    return result_list
```
## Max depth of a binary tree
* We use a Top-Down recursive approach to calculate the depth of a binary tree. 
* Top-Down recurison can kind of be thought like doing a preorder traversal, all we are doing is visiting each node, taking its value and passing it to its children.
* To find the max depth of a tree:
1. We know that the root of the tree always has depth 1
2. So all we need to do is recurse left down each branch of the tree, to its leaves. 
3. We can see we have two methods findLeft and findRight which do this recursion, we can also see that each time we move down to a new NON-NONE node we add 1 to the value.
4. Finally when we hit a leaf, we hit the condition root.left is None and root.right is None, so we want to return 1 to account for the depth of our leaf node and then we want to break out of the recursion for the specific left or right calls.
5. We then simply return the max of findLeft and findRight which returns to us the maximum depth of the tree.
```
def maxDepth(self, root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    findLeft = 1 + self.maxDepth(root.left)
    findRight = 1 + self.maxDepth(root.right)
    return max(findLeft, findRight)
```
* A binary tree is symmetric if the left subtree from the root and the right subtree from the root are mirrors of eachother.
1. All we need to do is make a new function, which will hold "copies" of the same tree
2. We then simply need to check in each iteration if the values of the nodes are the same and most importantly we need to check if the left branch of the left subtree == right branch of the right subtree and vice versa. 
3. This is the most important thing to realise! The recursive checkSubtrees(t1.left, t2.right) and checkSubtrees(t1.right, t2.left) are the most important calls here as they check for the symmetry between both left and right subtrees by comparing opposite ends.
```
def isSymmetric(self, root):
    return checkSubtrees(root, root)
def checkSubtrees(t1, t2):
    if t1 is None and t2 is None: return True
    if t1 is None or t2 is None: return False
    return t1.val == t2.val and checkSubtrees(t1.left, t2.right) and checkSubtrees(t1.right, t2.left)
```
## PathSum
1. Main idea here is just to understand the recursion, each call we are recursing into the left and right subtrees continuously until we hit our elif statement
2. Our elif condition simply checks if the node we are currently at is a leaf and if the value of that leaf is the remainder needed to deduct from targetSum, to reach our target.
3. Important thing here is to just visualize the traversal of the tree, the fact that every node in the tree will be visited and that each recursive call we are deducting our current node value from the targetSum
4. By deducting the current node value from the targetSum we are doing the same operation as adding up each node in the respective path to see if it equals the targetSum.
```
def hasPathSum(self, root, targetSum):
    if root == None:
        return False
    elif root.left == None and root.right == None and targetSum - root.val == 0:
        return True
    else:
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
```
## Build binary tree from inorder and postorder traversal lists 
* Firstly, recall inorder is left, root, right and postorder is left, right, root.
* Intuition here is that we know given a postorder traversal list, that from the end of the list, we have our main root, then each consecutive element is a root of a subtree going from the right to left subtrees.
* The idea here is that the element at the very end of the postorder list is going to be the main root of the tree. Hence, if we take that element, and we locate it in our inorder traversal list.
* We will find what the left and right subtrees are, as all the values in the inorder list from the beginning and up to and not including the root compromise the left subtree. All the values from after the root value till the end of the inorder list compromise the right subtree.
* The next thing you may think is "Ok, but how do I find the roots of each left and right subtree?" This is where postorder traversal knowledge comes in, we know that from the end of the post order traversal list we have all the roots, in particular from the right to left subtree.
* Therefore, all we need to do is simply recursivley build our right subtree first using the elements popped of from the end of the postorder list which is the right subtree root nodes, then once our inorder list is empty, this means there are no more nodes to add for the right subtree.
* So, our right recursive calls finish and we then move on and build our left subtree. Finally once the inorder list hits None, this means all nodes have been placed and our binary tree is made so return the root.
* Note the problem here is we are doing a lot of work! It is not very efficient in terms of auxillary memory usage, in particular, each recursive call we are passing a new list element(inorder) so o(n^2) auxillary space usage. We can do better! 
```
def buildTree(inorder, postorder):
    def recurse(inorder, postorder):
        if not inorder or not postorder: return
        root = TreeNode(postorder.pop())
        root.right = recurse(inorder[inorder.index(root.val) + 1:], postorder)
        root.left = recurse(inorder[:inorder.index(root.val)], postorder)
        return root
    return recurse(inorder, postorder)
```
## Build binary tree from inorder and postorder traversal lists OPTIMIZED
* We can optimize our solution as instead of usng  having to find the index each time we can use a hashmap.
* Set a hashmap to contain the element and indexes of the inorder list
* Use this hashmap to index in and find the respective elements from mid
* Like binary search where we have a left or right index we recursivley pass from mid+1 till max for the right subtree and min to mid-1 for the right subtree
```
def buildTree(inorder, postorder):
    hashMap = {inorder[i]: i for i in range(len(inorder))}
    def recurse(minVal, maxVal):
        if minVal > maxVal: return
        root = TreeNode(postorder.pop())
        midVal = hashMap[root.val]
        root.right = recurse(midVal + 1, maxVal)
        root.left = recurse(minVal, midVal - 1)
        return root
    return recurse(0, len(inorder) - 1)
```
## Build binary tree from inorder and preorder traversal lists OPTIMIZED
* This is the optimal way to build a binary tree using inorder and preorder lists.
* Once again same pattern as building a postorder and inorder tree algorithm. Alll we are doing is just popping from the front of the preorder list
* Remember this hashmap and binary search sort of pattern!
```
def buildTree(preorder, inorder):
    hashMap = {value: index for index, value in enumerate(inorder)}
    def recurse(minVal, maxVal):
        if minVal > maxVal: return
        root = TreeNode(preorder.pop(0))
        mid = hashMap[root.val]
        root.left = recurse(minVal, mid - 1)
        root.right = recurse(mid + 1, maxVal)
        return root
    return recurse(0, len(inorder) - 1)  # (36 ms, faster than 99.21%, 18.1 MB, less than 90.83%)
```
## Build binary tree from preorder traversal list using indexes
* Here we build a tree using just the preorder list and a index.
* The idea here is simply in a preorder list, every element at the ODD index is at the left subtree and every element at an EVEN index is in the right subtree * 2 for both.
```
def buildTree(preorder, inorder):
    def indexConstruct(preorder, index):
        if index >= len(preorder): return
        root = TreeNode(preorder[index])
        root.left = indexConstruct(preorder, 2 * index + 1)
        root.right = indexConstruct(preorder, 2 * index + 2)
        return root
    return indexConstruct(preorder, 0)
```
## Populating Next Right Pointers in Each Node Only Perfect Binary Tree
* Idea is we have a perfect binary tree. So we know that means that at each level there is 2**level-1 nodes.
 1. Lets start at the root of the binary tree and assign that value to leftmost.
 2. Then we are going to check its left child. While the left child is not none we iterate.
 3. We set head to point to the root initially, then as we go it will be the next left child
 4. While the head which will hold the left children does not equal none, we are going to set the left child of the parent(head) to the right child.
 5. We also need to check incase we need to make a connection but the parent is different. In this case we check if our current head node is not the only node remaining.
 6. If this case is true, we move to our current parents(heads) right child and connect that to the left child of the parent node after head.
 7. This sounds confusing, but I want you to imagine a perfect binary tree at its 2nd level, there are two parents, imagine their children.
 8. We connect the rightmost child node on the 3rd level of the leftmost parent on the 2nd level with the leftmost child node on the 3rd level of the rightmost parent on the 2nd level.
 9. This is why we do head.right.next = head.next.left
 10. Finally increment your head to he next node and once it hits None move leftmost to the leftmost node and repeat. 
```
def connect(root):
    if not root: return

    leftmost = root

    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left
    return root
```
## Populating Next Right Pointers in Each Node Any Binary Tree
1. We have a Binary Tree, it is NOT necessarily a perfect or balance binary tree. Note this as it is important. What we want to do is connect each node to its corresponding right node, if there is none connect to null.
2. Approach is that we make a Queue and add the head node of our current tree to the queue.
3. Then we set up a nested loop, the outer while loop iterates while the queue is not empty, hence while we have not visited every single node in the queue.
4. The inner loop iterates while we have not visited every single node on each respective level.
5. What we do is as we visit every node we check, is our current node the last node in the level, we do this check by saying is i < size - 1.
6. If our current node is NOT the last node in the level, we want to connect it to the adjacent node which is the direct next node in the queue. 
7. Thus we use queues FIFO property and make the next node of our current node to the element at the front of the queue which is the right adjacent node on the same level.
8. We also continue to add the children of each node we look at to our queue as we progress. Therefore everytime we iterate a level by the end of the iteration the new level is ready. 
```
class NextRightPointerBT {
    public Node connect(Node root) {
        if (root == null) {
            return root;
        }
        Queue<Node> Q = new LinkedList<Node>();
        Q.add(root);
        
        while (Q.size() > 0) {
            int size = Q.size();
            for (int i = 0; i < size; i++) {
                Node node = Q.poll();
                if (i < size - 1) {
                    node.next = Q.peek();
                } 
                if (node.left != null) {
                    Q.add(node.left);
                }
                if (node.right != null) {
                    Q.add(node.right);
                }
            }  
        } return root;
    }   
}
```
## Lowest Common Ancestor in Binary Tree
![1](https://user-images.githubusercontent.com/57751792/110291570-f02aae00-8050-11eb-8e74-6d49f48bc3fd.jpg)
![1](https://user-images.githubusercontent.com/57751792/110291579-f1f47180-8050-11eb-827e-8f8e0b1dc501.jpg)
```    
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // if root is null return null as it is not p or q.
        if (root == null) return null;
        // Check if root is p or q each call, if it is return root as we have found one of the nodes.
        if (root == p || root == q) return root;
        // Recurse down the left subtree, look for p or q, if we find it we are returned p or q else if it is NOT in the left subtree we are returned null and move onto the right subtree.
        TreeNode leftSubtree = lowestCommonAncestor(root.left, p, q);
        // Recurse down the right subtree, look for p and q, if we find it we are returned p or q else if it is NOT in the right subtree we are returned null and move onto our conditionals.
        TreeNode rightSubtree = lowestCommonAncestor(root.right, p, q);
        // Check if the current node we are at has two NOT NULL left right children, these children can only possibly be p and q therefore, the FIRST node to have TWO children is the LOWEST COMMON ANCESTOR. Return that node.
        if (leftSubtree != null && rightSubtree != null) return root;
        // If both the left and right nodes are null this parent node is NOT a ancestor hence return null.
        if (leftSubtree == null && rightSubtree == null) return null;
        // If ONE of the left or right nodes are NOT null, then we have found ONE of our required nodes, hence return the node we found and move back UP the recursive call stack.
        return (leftSubtree != null) ? leftSubtree:rightSubtree;
    }
}
```
## Count Univalue Subtrees
1. To solve this problem we are going to use a bottom up approach.
2. This will work well because we know that a leaf is a valid subtree, so if a leaf is a valid subtree then we are going to count it as a univalue subtree, and as we move up our tree we are easily able to check WHERE the subtree changes value hence where it is no longer a univalue subtree IF it occurs.
3. So set up a counter and set up a recursive function. We pass our root to the recursive function.
4. The process IN the recursive function is simple.
5. Firstly, if the root hence the NODE we are currently at is None this means that the parents MAY be a leaf hence we return True as if it is a leaf it could POSSIBLY be a univalue subtree, so we need to increment.
6. Next we reurse down the tree from the left, then from the right so a postorder traversal. Once we hit a leaf our recursion will BREAK and we will have True and True in left and right respectivley.
7. We then want to check, the following cases.
* Case 1: Is the left node None and right Node the same value as the parent? If so then return True because this is valid.
* Case 2: Is the right node None and left node the same value as the parent? If so then return True as valid univalue subtree.
* Case 3: As we have a OR statement if both children are the same value as the root we would return True anyway.
8. So in all of these instances if we returned True this implies we have a univalue subtree hence increment the counter. Else return False, this is NOT a univalue subtree as the parent is DIFFERENT. So return to the previous call and repeat the recursion.
```
def countUnivalSubtrees(self, root):
    self.count = 0
    self.recurse(root)
    return self.count


def recurse(self, root):
    if not root: return True
    left = self.recurse(root.left)
    right = self.recurse(root.right)
    if left == True and right == True and (root.left == None or root.left.val == root.val) and (
            root.right == None or root.right.val == root.val):
        self.count += 1
        return True
    return False
```
## Maximum path in binary tree
1. Firstly, understand what the question wants. It wants the MAX PATH. Recall a path is a sequence or iteration of nodes in a binary tree where there are no cycles.
2. Now, I want you to approach the recursion this way - "What work do I want to do at EACH node?" Well at each node we want to find the value of its left and right subtrees and take the MAX between those to subtrees as this SPECIFIC nodes path.
3. No this is seen by our calls to left_subtree and right subtree, think of it as EACH node in the binary tree saying "hey I want the value of MY left subtree and MY right subtrees. If there negative, well I don't want em! Else I will gladly take em!".
4. Then after we have found the MAX values of the node which we are currently looking at, imagine our node says this "OK, so this is MY value, and here is the value of my two children which may or may not be subtrees i don't really care, oh and they are not gonna be negative don't worry!"
5. We then will record the max_path everytime! Think dp style.
6. Finally we will return the current nodes MAX path! Now this is where you may mess up, Imagine this:
           3
             \
                5
               / 
              6
            /   \
           7     8
 * Now if your taking the max path of 5 well would you take the sum of BOTH 7 & 8 leaves? No because this is not a path! As to do so we would have a REPETITION! 6 would be repeated and we know that we cannot repeat any nodes in a path!
 * This is the reason WHY we have to take the maximum value between the left and right subtrees otherwise we get repetition and we DON'T have a valid path! 
```
def maxPathSum(self, root: TreeNode) -> int:
    max_path = root.val

    def findMaxPath(root):
        nonlocal max_path
        if not root: return 0
        left_subtree = max(findMaxPath(root.left), 0)
        right_subtree = max(findMaxPath(root.right), 0)
        max_path = max(max_path, root.val + left_subtree + right_subtree)
        return root.val + max(left_subtree, right_subtree)

    findMaxPath(root)
    return max_path
```
## All root to leaf paths in binary tree
1. Idea here is we want to return a list of strings which contains all of the root to leaf paths in the binary tree.
2. So initialize a list (path_list) then we are going to make a recursive call function. In the function we will pass the root of the binary tree and a empty string which we will modify and add node values as we recurse.
3. If the root is NOT none, we want to add that node value to our string, this will always begin from the ROOT of the binary tree. This will build our string of paths.
4. Once we come accross a leaf our second condition will be met thus we know that if we hit a leaf we have reached the END of the path, so we have our root to leaf path, hence we should add that path to our path_list, not path_list will be global for inner function.
5. Otherwise if we are not at a leaf, we still want to build our list and add the node value BUT we want to keep recursing down the tree until we hit the leaves, so we simply recurse left and right respectivley.
6. Rememeber to pass the path + -> as this will build the string according to the desired output. Done! 
```
def binaryTreePaths(self, root):
    path_list = []
    def recurse(root, path):
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                path_list.append(path)
            else:
                recurse(root.left, path + "->")
                recurse(root.right, path + "->")
    recurse(root, "")
    return path_list
```
## Number of islands
1. Idea is we are going to do a simple linear traversal through the matrix.
2. Whenever we come across "land" which is a '1' char, we are going to increment our land counter and we are going to get "rid" of the land.
3. So we want to "get rid of" the land because there may be multiple islands which are not connected, hence we need to visit those islands and increment our counter!
4. Now it is actually quite a simple process to get "rid of the land", all we do is a simple DFS recursive call once we find our first 1 in the linear traversal.
5. The dfs recursion will visit the top, bottom, left, right elements in the matrix respectively and transform them into 0's, and we know that 0 = water = our linear traversal will not halt on it.
6. Thus thats it! Not to bad at all, just traverse, find the land, remove the land with top-bottom-left-right dfs, move onto next land, repeat until matrix finished.
Time complexity: O(M * N) because of the matrix traversal
Space complexity: O(n) if all elements are '1' in the matrix for the call stack
```
public class NumberOfIslands {
        public int numIslands(char[][] grid) {
        int islands = 0;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[row].length; col++) {
                if (grid[row][col] == '1') {
                    dfs(grid, row, col);
                    islands++;
                }
            }
        } return islands;
    }
    private void dfs(char[][] grid, int row, int col) {
        if (row >= 0 && col >= 0 && row < grid.length && col < grid[row].length && grid[row][col] == '1') {
            grid[row][col] = '0';
            dfs(grid, row - 1, col); // Top
            dfs(grid, row + 1, col); // Bottom
            dfs(grid, row, col - 1); // Left
            dfs(grid, row, col + 1); // Right
        }
    }
}
```
## WordLadder
![1](https://user-images.githubusercontent.com/57751792/110726267-fc478300-827d-11eb-95ff-640438e96d5f.jpg)
![1](https://user-images.githubusercontent.com/57751792/110726272-fea9dd00-827d-11eb-8337-0f9e9ec6c91e.jpg)
![1](https://user-images.githubusercontent.com/57751792/110726278-ffdb0a00-827d-11eb-845d-04a33ad0780b.jpg)
![1](https://user-images.githubusercontent.com/57751792/110726283-01a4cd80-827e-11eb-9394-a38c3788d410.jpg)
```
import java.util.*;


public class WordLadder {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Queue<String> queue = new LinkedList<>(); // Queue to do BFS of the graph we are going to build.
        Set<String> wordSet = new HashSet<>(wordList); // NOTE THIS IS HOW YOU ADD A LIST OF WORDS TO HASHSET!
        wordSet.remove(beginWord); // Remove the beginning word from set
        queue.add(beginWord); // Add it to queue to build first level
        int level = 0;

        while (!queue.isEmpty()) {
            level++; // Increment level as we iterate
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String currentWord = queue.poll(); // Current word node at level
                if (currentWord.equals(endWord)) return level; // Found the endWord in the queue so we are done
                List<String> allSeqList = findSeqs(currentWord); // Get an array holding all possible sequences
                for (String s: allSeqList) { //For every possible sequence in the array in respect to currentword
                    if (wordSet.contains(s)) { // If the particular sequence is in the hashSet
                        wordSet.remove(s); // Remove that element from the hashset as we have visited it
                        queue.add(s); //Add it to the next level of the queue.
                    }
                }
            }
        } return 0;
    }

    public static List<String> findSeqs(String currentWord) {
        char[] charArray = currentWord.toCharArray(); // Make a list of chars so each individual char from cWord
        List<String> allPossSeqs = new ArrayList<>(); // Array to hold all combinations of the word
        for (int i = 0; i < charArray.length; i++) { // For every single CHAR in the passed word. This is important because recall we want to change EVERY single char to get ALL possible combinations.
            char temp = charArray[i]; // We need a temp char so we can eventually revert back.
            for (char c = 'a'; c <= 'z'; c++) { // This sets c to go from a - z hence the entire alphabet
                charArray[i] = c; // Make the CURRENT char we are looking at = to each alphabet character
                String nextSeq = new String(charArray);// Convert the current charArray WITH the transformed letter to a string and add that string to all possible sequences array.
                allPossSeqs.add(nextSeq); // Add this combination to our combinations array
            }
            charArray[i] = temp; // Revert the character back to original and move onto the next one in the word.
        }
        return allPossSeqs; // Return array of all possible combinations of passed argument currentWord
    }
}
```
## Validate a BST
![1](https://user-images.githubusercontent.com/57751792/111106805-a561e680-85ba-11eb-9731-bdda7b812990.jpg)
```
public class IsValidBST {
    public boolean isValidBST(TreeNode root) {
        return DFS(root, null, null);
    }

    private boolean DFS(TreeNode root, Integer low, Integer high) {
        if (root == null) return true;

        if (low != null && low >= root.val)
            return false;
        if (high != null && high <= root.val)
            return false;
        return DFS(root.left, low, root.val) && DFS(root.right, root.val, high);
    }
}
```
## Diameter of binary tree
```
def diameterOfBinaryTree(self, root):
    diameter = 0

    def dfs(root):
        nonlocal diameter
        if not root: return 0
        left = dfs(root.left)
        right = dfs(root.right)
        diameter = max(diameter, left + right)
        return max(left, right) + 1

    dfs(root)
    return diameter
```
## Flip equivalent binary trees
1. Given two binary trees we want to check whether the second binary tree is the same as the first but with flipped left and right subtrees.
2. Idea is to use DFS traversal and compare the respective node and left and right subtree values as we recurse.
3. Start with checking if the root values are equal, hence node values are equal.
4. Then we check for all of our false cases, being if either nodes are null or if the values are not equal
5. Finally we recursively check if the left and right subtrees are indeed equal. This is done by either checking dfs(left,left) && dfs(right,right) || dfs(left, right) && dfs(right, left) because remember the tree can be flipped.
6. Time complexity = O(n) as we iterate through all nodes in both trees.
7. Space complexity = O(h) h being the height of the largest of the two binary trees.
```
public class FlipEquivBinaryTree {
        public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        if (root1 == root2) return true;
        if (root1 == null || root2 == null || root1.val != root2.val) return false;
        return flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right) ||
               flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left);
    }
}
```
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
* Idea is the list in question "height" depicts the possible water levels at each specific index.
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
# Bit Manipulation
## Basics
* 1 = True and 0 = False
* AND = & = only true if true and true (1 & 1)
* XOR = ^ = Only true if either true else false (1 & 0 or 0 & 1) NOT true for (1 & 1)
* <<  = Shift left = Shifts all bits left by n, default input values is 0.
* Please view image below for more detail
![1](https://user-images.githubusercontent.com/57751792/111941299-9f798180-8b35-11eb-89e9-30c04a9ebdeb.png)
## Sum two integers without + operator
1. First of all if you ever see any question which asks to conduct a arithmetic operation without operators the first thing you should think of is bit manipulation.
2. Now, Idea here is the following:
* & = Carry
* ^ = Addition
* << = Shifting the carry.
3. The AND operator is used to find the carry, try this out for yourself with some simple binary arithemtic, you will see that the AND input is equivalent to the carry BUT it just is not shifted left as it should be, which is where the bit shift operator comes in as it will shift the AND bit hence the carry bit left as it should each iteration.
4. THe XOR ^ operator will be used to compute the addition each iteration but it will not include the carry, this is why & and << is needed.
5. I want you to just imagine that in each iteration, we are working with ONE of the bits for each value at a time and computing the addition value and carry.
6. Once the carry hits 0000 so fully 0 this indicates we are done, hence , return the value.
7. Here is a visual depicition:
![1](https://user-images.githubusercontent.com/57751792/111942038-5f1b0300-8b37-11eb-80c6-dfb5abc641ab.png)
```
public class SumTwoIntegers {
    public static int SumTwoIntegers(int a, int b) {
        while (b != 0) {
            int addition = a ^ b;
            int carryShift = (a & b) << 1;
            a = addition;
            b = carryShift;
        }
        return a;
    }
```
## Bin() operator
bin() will return the string binary represenation of a given integer value with 0b tacked on the front. Super useful opeartor so keep it in mind. 
## Here is a nice implementation of bin() in a problem where we need to return number of 1 bits per elements in an array of integers
```
def countBits(self, nums):
    return [len(bin(i)[2:].replace("0", "")) for i in range(nums + 1)]
```
## Missing number in unsorted array
1. Recall XOR properties:
* a ^ a = 0
* a ^ 0 = a
* XOR = True IFF values differ, if equal then False
2. So this can be applied nicely to our problem, where we want to find the missing number in an array in O(n) time and O(1) space.
3. Let len(nums) = 5 then xor = 5.
4. Let nums = [2, 5, 3, 1, 6]
5. Then we iterate through every element in nums and what we are doing is building an XOR value our XOR variable will look like this:
6. xor = 5 ^ 2 ^ 0 ^ 5 ^ 5 ^ 1 ^ 5 ^ 3 ^ 2 ^ 5 ^ 1 ^ 3 ^ 5 ^ 1 ^ 4 ^ 5 ^ 6 ^ 5
7. What we notice here is that every value appears at least twice EXCEPT for 4! Which is the missing value.
8. Now due to the property of XOR of a ^ a = 0, all the numbers which appear multiple times will be 0 BUT the other property a ^ 0 = a will also be applied on the number which only appeared once.
9. This number which only appears once is the missing value and the XOR operaton will find it as it will do a ^ 0 = a, which will be the remaining value left in the xor variable.
```
def missingNumber(self, nums):
    xor = len(nums)
    for i in range(len(nums)):
        xor = xor ^ nums[i] ^ i
    return xor
```
