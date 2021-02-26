#* Here we build a tree using just the preorder list and a index.
#* The idea here is simply in a preorder list, every element at the ODD index is at the left subtree and every element at an EVEN index is in the right subtree * 2 for both.
def buildTree(preorder, inorder):
    def indexConstruct(preorder, index):
        if index >= len(preorder): return
        root = TreeNode(preorder[index])
        root.left = indexConstruct(preorder, 2 * index + 1)
        root.right = indexConstruct(preorder, 2 * index + 2)
        return root
    return indexConstruct(preorder, 0)