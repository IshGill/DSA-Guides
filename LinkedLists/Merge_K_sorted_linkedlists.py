# Given a list which contains K linked lists to merge them into one sorted linked list the simplest idea seems to be to transfer all the elements in the list of linked lists into a single linked list
# The transfer all the elements of the single linked list into a simple array, sort the array, then make a new linked list add all the elements from the array in sorted order and voila!
# Time complexity o(n log n) as we need to iterate though the linked lists and auxillary space usage is o(n) to! So we can improve there!

class Solution(object):
    def mergeKLists(lists):
        head = list2 = ListNode(0)
        for i in lists:
            current = i
            while current:
                list2.next = current
                current = current.next
                list2 = list2.next
        curr = head.next
        sortedArray = []
        while curr:
            sortedArray.append(curr.val)
            curr = curr.next
        sortedArray.sort()
        dummy = sortedLL = ListNode(0)
        for i in sortedArray:
            sortedLL.next = ListNode(i)
            sortedLL = sortedLL.next
        return dummy.next
