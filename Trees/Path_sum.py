# Idea here is that we are adding the value of the node in each recursive call. If the root is None then this means we have passed the leaves and not been able to return True, hence the target sum did not exist
# So whats happening is we pretty much divide the tree into left and right subtrees using recursion continuously in our last return statement. Each call we are recursing into the respective left and right subtrees subtree.
# You must think about this recurisvely, each return we make we are going into the left subtree of the current left subtree, we keep doing this unitl we hit None, then we begin the same process for the right subtree
# Using this recursive method we visit every single node and every path in our binary tree. Once we hit the leaves we have a condition which first of all checks for the leaves, of course we do a leaf check by checking if the left and right children of the current node are None
# We then need to understand that if we are at a leaf we have a path from the root hence we can answer our question, we check is the value left in target sum as we have been deducting targetsums value as we go thorugh the tree = to the value of the leaf, if it is then this implies this is a perfect path a perfect match meaning this path has nodes which sum up to the required sum

#1. Main idea here is just to understand the recursion, each call we are recursing into the left and right subtrees continuously until we hit our elif statement
#2. Our elif condition simply checks if the node we are currently at is a leaf and if the value of that leaf is the remainder needed to deduct from targetSum, to reach our target.
#3. Important thing here is to just visualize the traversal of the tree, the fact that every node in the tree will be visited and that each recursive call we are deducting our current node value from the targetSum
#4. By deducting the current node value from the targetSum we are doing the same operation as adding up each node in the respective path to see if it equals the targetSum.
def hasPathSum(self, root, targetSum):
    if root == None:
        return False
    elif root.left == None and root.right == None and targetSum - root.val == 0:
        return True
    else:
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)