/*
package Leetcode;

import javax.swing.tree.TreeNode;

public class IsValidBST {
    public boolean isValidBST(TreeNode root) {
        return DFS(root, null, null);
    }

    private boolean DFS(TreeNode root, Integer low, Integer high) {
        if (root == null) return true;

        if (low != null && low >= root.val)
            return false;
        if (high != null && high <= root.val)
            return false;
        return DFS(root.left, low, root.val) && DFS(root.right, root.val, high);

    }
}
}
*/