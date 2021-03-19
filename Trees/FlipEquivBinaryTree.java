package Leetcode;

class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }
/*
1. Given two binary trees we want to check whether the second binary tree is the same as the first but with flipped left and right subtrees.
2. Idea is to use DFS traversal and compare the respective node and left and right subtree values as we recurse.
3. Start with checking if the root values are equal, hence node values are equal.
4. Then we check for all of our false cases, being if either nodes are null or if the values are not equal
5. Finally we recursively check if the left and right subtrees are indeed equal. This is done by either checking dfs(left,left) && dfs(right,right) || dfs(left, right) && dfs(right, left) because remember the tree can be flipped.
6. Time complexity = O(n) as we iterate through all nodes in both trees.
7. Space complexity = O(h) h being the height of the largest of the two binary trees.
 */
public class FlipEquivBinaryTree {
        public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        if (root1 == root2) return true;
        if (root1 == null || root2 == null || root1.val != root2.val) return false;
        return flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right) ||
               flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left);
    }
}

