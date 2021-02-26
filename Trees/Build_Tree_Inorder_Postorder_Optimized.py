#* We can optimize our solution as instead of usng  having to find the index each time we can use a hashmap.
#* Set a hashmap to contain the element and indexes of the inorder list
#* Use this hashmap to index in and find the respective elements from mid
#* Like binary search where we have a left or right index we recursivley pass from mid+1 till max for the right subtree and min to mid-1 for the right subtree
def buildTree(inorder, postorder):
    hashMap = {inorder[i]: i for i in range(len(inorder))}
    def recurse(minVal, maxVal):
        if minVal > maxVal: return
        root = TreeNode(postorder.pop())
        midVal = hashMap[root.val]
        root.right = recurse(midVal + 1, maxVal)
        root.left = recurse(minVal, midVal - 1)
        return root
    return recurse(0, len(inorder) - 1)