# Inorder = left, print, right. DFS = Moving down the binary tree, depth of the tree.
def inorderTraversal(self, root):
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root != None else []