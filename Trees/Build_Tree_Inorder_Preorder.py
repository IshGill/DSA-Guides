#* Same pattern as inorder to postorder!
#* We know that preorder is root, left, right, hence we just pop from the front of the preorder list, we use that value as the root and assign left and right subtrees accordingly.
#* This is NOT and optimal method, but I want to show it as it provides good intuition on how to approach these problems.
def buildTree(preorder, inorder):
    def recurse(preorder, inorder):
        if not inorder: return
        root = TreeNode(preorder.pop(0))
        mid = inorder.index(root.val)
        root.left = recurse(preorder, inorder[:mid])
        root.right = recurse(preorder, inorder[mid + 1:])
        return root
    return recurse(preorder, inorder)