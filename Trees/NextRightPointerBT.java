package Leetcode;
import org.w3c.dom.Node;
import java.util.LinkedList;
import java.util.Queue;
/*
1. We have a Binary Tree, it is NOT necessarily a perfect or balance binary tree. Note this as it is important. What we want to do is connect each node to its corresponding right node, if there is none connect to null.
2. Approach is that we make a Queue and add the head node of our current tree to the queue.
3. Then we set up a nested loop, the outer while loop iterates while the queue is not empty, hence while we have not visited every single node in the queue.
4. The inner loop iterates while we have not visited every single node on each respective level.
5. What we do is as we visit every node we check, is our current node the last node in the level, we do this check by saying is i < size - 1.
6. If our current node is NOT the last node in the level, we want to connect it to the adjacent node which is the direct next node in the queue.
7. Thus we use queues FIFO property and make the next node of our current node to the element at the front of the queue which is the right adjacent node on the same level.
8. We also continue to add the children of each node we look at to our queue as we progress. Therefore everytime we iterate a level by the end of the iteration the new level is ready.
 */
class NextRightPointerBT {
    public Node connect(Node root) {
        if (root == null) {
            return root;
        }
        Queue<Node> Q = new LinkedList<Node>();
        Q.add(root);

        while (Q.size() > 0) {
            int size = Q.size();
            for (int i = 0; i < size; i++) {
                Node node = Q.poll();
                if (i < size - 1) {
                    node.next = Q.peek();
                }
                if (node.left != null) {
                    Q.add(node.left);
                }
                if (node.right != null) {
                    Q.add(node.right);
                }
            }
        } return root;
    }
}
