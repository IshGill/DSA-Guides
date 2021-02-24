# 1. Check if the root is empty, hence if the tree is empty.
# 2. We are going to use queues to solve this problem as the queue FIFO property works well here.
# 3. Initialize a queue to hold the current root node
# 4. level is going to be an empty list/queue which we use to add in all the nodes at the particular level in the tree
# 5. next queue is going to hold the nodes in the NEXT level of the binary tree
# 6. result will store our nested list representation of the level order of the tree
# * The main idea is that starting off with the root, we loop thorugh all the nodes level by level, we add the nodes at each respective level to the level queue and we add their children to the next queue
# * After the end of each loop we transfer the nodes at the respective level into our results queue, we now want to look at the next level in the tree, hence we assign our queue to point to the next_queue variable which holds the next level nodes.
# * We empty the next_queue variable and level queues and repeat this same process until there are no more nodes left to visit.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def levelOrder(root):
    #      3
    #     / \
    #    9  20
    #      /  \
    #    15    7
    # q = [3]; level = [3]; next_q = [9, 20]; result =[]
    if not root: return []
    queue = [root]
    level = []
    next_queue = []
    result = []
    while queue:
        for root in queue:
            level.append(root.val)
            if root.left:
                next_queue.append(root.left)
            if root.right:
                next_queue.append(root.right)
        result.append(level)
        queue = next_queue
        next_queue = []
        level = []
    return result
