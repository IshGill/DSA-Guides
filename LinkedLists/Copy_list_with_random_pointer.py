#* We make a hash table and simply do two passes through our given linked list in question.
#* First pass we make the key of the hash table equal to the reference in memory of each respective node in the linked list and the value in the hash table will be a NEW node element which has the same VALUE as the current node we are looking at.
#* So now we have a hash table which contains values which are nodes with no connections to any other nodes, they are just sitting there waiting to be connected up. We also have keys which are the memory references which allow us to index in with O(1) time.
#* We now do our second pass, we are now going the make the connections for the copied nodes in the hash table.
#* We set the next node of the copied node "hashMap[current].next" as the next node of the corresponding key in the hash table, meaning the next node of the original node in the linked list.
#* We set the random node for the copied node "hashMap[random].next" as the random node for the original node in the original linked list.
#* Make sure to check that the nodes do not equal none for random or next.
#* Finally we return the hashMap values which are going to be connected now as a linked list from the head value. 
def copyRandomList(head):
    if not head: return None
    current = head
    hashMap = {}

    while current:
        hashMap[current] = Node(current.val, None, None)
        current = current.next

    current = head
    while current:
        if current.next:
            hashMap[current].next = hashMap[current.next]
        if current.random:
            hashMap[current].random = hashMap[current.random]
        current = current.next
    return hashMap[head]