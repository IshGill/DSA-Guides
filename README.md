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
* Iterative solution
* [EXPLANATION]

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

def countUnivalSubtrees(self, root):
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
