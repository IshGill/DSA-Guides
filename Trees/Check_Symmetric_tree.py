#* A binary tree is symmetric if the left subtree from the root and the right subtree from the root are mirrors of eachother.
#1. All we need to do is make a new function, which will hold "copies" of the same tree
#2. We then simply need to check in each iteration if the values of the nodes are the same and most importantly we need to check if the left branch of the left subtree == right branch of the right subtree and vice versa.
#3. This is the most important thing to realise! The recursive checkSubtrees(t1.left, t2.right) and checkSubtrees(t1.right, t2.left) are the most important calls here as they check for the symmetry between both left and right subtrees by comparing opposite ends.

def isSymmetric(self, root):
    return checkSubtrees(root, root)
def checkSubtrees(t1, t2):
    if t1 is None and t2 is None: return True
    if t1 is None or t2 is None: return False
    return t1.val == t2.val and checkSubtrees(t1.left, t2.right) and checkSubtrees(t1.right, t2.left)