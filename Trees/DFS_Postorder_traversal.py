# Postorder = left, right, print. 
def postorderTraversal(root):
    return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []