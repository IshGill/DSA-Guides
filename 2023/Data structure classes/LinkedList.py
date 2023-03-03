class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.head
        counter = 0
        if curr is None:
            return -1 
        elif index >= self.size or index < 0:
            return -1
        else:
            while curr is not None:
                if counter == index:
                    return curr.val 
                else:
                    curr = curr.next
                    counter += 1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next != None:
                curr = curr.next
            curr.next = Node(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node

            self.size += 1
            
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        curr = self.head
        counter = 0
        if index > self.size or index < 0:
            return
        elif index == 0:
            self.head = curr.next
            self.size -= 1
            return 
        else:
            while curr is not None:
                if counter == index - 1:
                    if curr.next is not None:
                        curr.next = curr.next.next 
                        self.size -= 1
                        return
                curr = curr.next
                counter += 1