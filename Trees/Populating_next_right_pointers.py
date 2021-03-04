# * Idea is we have a perfect binary tree. So we know that means that at each level there is 2**level-1 nodes.
# 1. Lets start at the root of the binary tree and assign that value to leftmost.
# 2. Then we are going to check its left child. While the left child is not none we iterate.
# 3. We set head to point to the root initially, then as we go it will be the next left child
# 4. While the head which will hold the left children does not equal none, we are going to set the left child of the parent(head) to the right child.
# 5. We also need to check incase we need to make a connection but the parent is different. In this case we check if our current head node is not the only node remaining.
# 6. If this case is true, we move to our current parents(heads) right child and connect that to the left child of the parent node after head.
# 7. This sounds confusing, but I want you to imagine a perfect binary tree at its 2nd level, there are two parents, imagine their children.
# 8. We connect the rightmost child node on the 3rd level of the leftmost parent on the 2nd level with the leftmost child node on the 3rd level of the rightmost parent on the 2nd level.
# 9. This is why we do head.right.next = head.next.left
# 10. Finally increment your head to he next node and once it hits None move leftmost to the leftmost node and repeat. 
def connect(root):
    if not root: return

    leftmost = root

    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left
    return root
