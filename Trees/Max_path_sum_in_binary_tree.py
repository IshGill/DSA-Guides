#1. Firstly, understand what the question wants. It wants the MAX PATH. Recall a path is a sequence or iteration of nodes in a binary tree where there are no cycles.
#2. Now, I want you to approach the recursion this way - "What work do I want to do at EACH node?" Well at each node we want to find the value of its left and right subtrees and take the MAX between those to subtrees as this SPECIFIC nodes path.
#3. No this is seen by our calls to left_subtree and right subtree, think of it as EACH node in the binary tree saying "hey I want the value of MY left subtree and MY right subtrees. If there negative, well I don't want em! Else I will gladly take em!".
#4. Then after we have found the MAX values of the node which we are currently looking at, imagine our node says this "OK, so this is MY value, and here is the value of my two children which may or may not be subtrees i don't really care, oh and they are not gonna be negative don't worry!"
#5. We then will record the max_path everytime! Think dp style.
#6. Finally we will return the current nodes MAX path! Now this is where you may mess up, Imagine this:
#           3
#             \
#                5
#               /
#              6
#            /   \
#           7     8
# * Now if your taking the max path of 5 well would you take the sum of BOTH 7 & 8 leaves? No because this is not a path! As to do so we would have a REPETITION! 6 would be repeated and we know that we cannot repeat any nodes in a path!
# * This is the reason WHY we have to take the maximum value between the left and right subtrees otherwise we get repetition and we DON'T have a valid path!
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