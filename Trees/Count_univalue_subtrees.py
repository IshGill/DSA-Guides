#1. To solve this problem we are going to use a bottom up approach.
#2. This will work well because we know that a leaf is a valid subtree, so if a leaf is a valid subtree then we are going to count it as a univalue subtree, and as we move up our tree we are easily able to check WHERE the subtree changes value hence where it is no longer a univalue subtree IF it occurs.
#3. So set up a counter and set up a recursive function. We pass our root to the recursive function.
#4. The process IN the recursive function is simple.
#5. Firstly, if the root hence the NODE we are currently at is None this means that the parents MAY be a leaf hence we return True as if it is a leaf it could POSSIBLY be a univalue subtree, so we need to increment.
#6. Next we reurse down the tree from the left, then from the right so a postorder traversal. Once we hit a leaf our recursion will BREAK and we will have True and True in left and right respectivley.
#7. We then want to check, the following cases.
#* Case 1: Is the left node None and right Node the same value as the parent? If so then return True because this is valid.
#* Case 2: Is the right node None and left node the same value as the parent? If so then return True as valid univalue subtree.
#* Case 3: As we have a OR statement if both children are the same value as the root we would return True anyway.
#8. So in all of these instances if we returned True this implies we have a univalue subtree hence increment the counter. Else return False, this is NOT a univalue subtree as the parent is DIFFERENT. So return to the previous call and repeat the recursion.

def countUnivalSubtrees(self, root):
    self.count = 0
    self.recurse(root)
    return self.count


def recurse(self, root):
    if not root: return True
    left = self.recurse(root.left)
    right = self.recurse(root.right)
    if left == True and right == True and (root.left == None or root.left.val == root.val) and (
            root.right == None or root.right.val == root.val):
        self.count += 1
        return True
    return False
