# Firstly, recall inorder is left, root, right and postorder is left, right, root.
#* Intuition here is that we know given a postorder traversal list, that from the end of the list, we have our main root, then each consecutive element is a root of a subtree going from the right to left subtrees.
#* The idea here is that the element at the very end of the postorder list is going to be the main root of the tree. Hence, if we take that element, and we locate it in our inorder traversal list.
#* We will find what the left and right subtrees are, as all the values in the inorder list from the beginning and up to and not including the root compromise the left subtree. All the values from after the root value till the end of the inorder list compromise the right subtree.
#* The next thing you may think is "Ok, but how do I find the roots of each left and right subtree?" This is where postorder traversal knowledge comes in, we know that from the end of the post order traversal list we have all the roots, in particular from the right to left subtree.
#* Therefore, all we need to do is simply recursivley build our right subtree first using the elements popped of from the end of the postorder list which is the right subtree root nodes, then once our inorder list is empty, this means there are no more nodes to add for the right subtree.
# So, our right recursive calls finish and we then move on and build our left subtree. Finally once the inorder list hits None, this means all nodes have been placed and our binary tree is made so return the root.
#* Note the problem here is we are doing a lot of work! It is not very efficient in terms of auxillary memory usage, in particular, each recursive call we are passing a new list element(inorder) so o(n^2) auxillary space usage. We can do better!
def buildTree(inorder, postorder):
    def recurse(inorder, postorder):
        if not inorder or not postorder: return
        root = TreeNode(postorder.pop())
        root.right = recurse(inorder[inorder.index(root.val) + 1:], postorder)
        root.left = recurse(inorder[:inorder.index(root.val)], postorder)
        return root

    return recurse(inorder, postorder)