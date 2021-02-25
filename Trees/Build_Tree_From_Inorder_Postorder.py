def buildTree(inorder, postorder):
    def recurse(inorder, postorder):
        if not inorder or not postorder: return
        root = TreeNode(postorder.pop())
        root.right = recurse(inorder[inorder.index(root.val) + 1:], postorder)
        root.left = recurse(inorder[:inorder.index(root.val)], postorder)
        return root

    return recurse(inorder, postorder)
