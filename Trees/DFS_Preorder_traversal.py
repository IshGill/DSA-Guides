# Preorder = print, left, right. DFS = moving down the tree. 
def preorderTraversal(self, root):
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root != None else []