# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
# root = [1, None, 2, 3], preorder = node, left, right, stack = LIFO therefore; stack = [right, left, root];
# root = 1; root.right = 2
# stack = [2]; result = [1]; root = 2; root.left = 3; stack = [3]; result = [1, 2]
# stack = [3]; root = 3;
#           1
#             \
#               2
#              /
#             3
        if not root: return []
        stack = [root]
        result = []
        while stack:
            root = stack.pop()
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            result.append(root.val)
        return result