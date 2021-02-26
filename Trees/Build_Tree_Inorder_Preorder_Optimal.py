#* This is the optimal way to build a binary tree using inorder and preorder lists.
#* Once again same pattern as building a postorder and inorder tree algorithm. Alll we are doing is just popping from the front of the preorder list
#* Remember this hashmap and binary search sort of pattern!
def buildTree(preorder, inorder):
    hashMap = {value: index for index, value in enumerate(inorder)}
    def recurse(minVal, maxVal):
        if minVal > maxVal: return
        root = TreeNode(preorder.pop(0))
        mid = hashMap[root.val]
        root.left = recurse(minVal, mid - 1)
        root.right = recurse(mid + 1, maxVal)
        return root
    return recurse(0, len(inorder) - 1)  # (36 ms, faster than 99.21%, 18.1 MB, less than 90.83%)