package Leetcode;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.ArrayList;


public class Serialize_deserialize_binary_tree {

 public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
  }

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        // Preorder traversal to build our string.
        if (root == null) return "#";
        String left = serialize(root.left);
        String right = serialize(root.right);
        return root.val + "," + left + "," + right;

    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        // We use a queue because we can deserialse in the same way we serialised (preorder)
        Queue<String> dserialised = new LinkedList<>();
        dserialised.addAll(Arrays.asList(data.split(",")));
        return helper(dserialised);
        }
        public TreeNode helper(Queue<String> dserialised) {
            String node = dserialised.poll();
            if (node.equals("#")) return null;
            TreeNode newNode = new TreeNode(Integer.valueOf(node));
            newNode.left = helper(dserialised);
            newNode.right = helper(dserialised);
            return newNode;
        }
}
}
