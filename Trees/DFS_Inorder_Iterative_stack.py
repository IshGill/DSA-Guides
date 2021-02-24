#* Inorder = left, node, right
#* Main idea is our main loop iterates while root or stack are both not empty/null.
#* The inner while loop is used to traverse to the left as far as possible. It build up our stack, and once we hit the leaf with no left child we break out of this loop
#* Once we break out of the left iterative loop, we pop off the last element pushed onto the stack, so the last left node with no left child, we append this value to our results list
#* We then want to iterate right and visit the right subtree of the same node. When we iterate right once, our inner left loop will rebegin and complete the process again of finding the leftmost node
#* Notice the pattern here! Inorder is left, node, right. We have two while loops, we begin by always going as far left as possible, when that break we add our node at the top of the stack, then we go right. Make sense yea.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
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