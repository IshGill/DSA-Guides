package Leetcode;

public class LowestCommonAncestor {
     public static class TreeNode {
         int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
        }

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // if root is null return null as it is not p or q.
        if (root == null) return null;
        // Check if root is p or q each call, if it is return root as we have found one of the nodes.
        if (root == p || root == q) return root;
        // Recurse down the left subtree, look for p or q, if we find it we are returned p or q else if it is NOT in the left subtree we are returned null and move onto the right subtree.
        TreeNode leftSubtree = lowestCommonAncestor(root.left, p, q);
        // Recurse down the right subtree, look for p and q, if we find it we are returned p or q else if it is NOT in the right subtree we are returned null and move onto our conditionals.
        TreeNode rightSubtree = lowestCommonAncestor(root.right, p, q);
        // Check if the current node we are at has two NOT NULL left right children, these children can only possibly be p and q therefore, the FIRST node to have TWO children is the LOWEST COMMON ANCESTOR. Return that node.
        if (leftSubtree != null && rightSubtree != null) return root;
        // If both the left and right nodes are null this parent node is NOT a ancestor hence return null.
        if (leftSubtree == null && rightSubtree == null) return null;
        // If ONE of the left or right nodes are NOT null, then we have found ONE of our required nodes, hence return the node we found and move back UP the recursive call stack.
        return (leftSubtree != null) ? leftSubtree:rightSubtree;
    }
}
}
