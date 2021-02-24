def maxDepth(self, root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    findLeft = 1 + self.maxDepth(root.left)
    findRight = 1 + self.maxDepth(root.right)
    return max(findLeft, findRight)

#     def maxDepth(self, root):
#         if root is None:
#             return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
