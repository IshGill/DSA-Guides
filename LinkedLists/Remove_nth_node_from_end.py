# * Dummy is the star here. By using dummy we are able to stay n + 1 behind runner, therefore we don't get any pesky edge case errors when current.next.next == None etc
# * So main thing to remember is use dummy, stay n + 1 behind and always return dummy.next.
def removeNthFromEnd(head, n):
    dummy = current = ListNode(0, head)
    runner = head
    for i in range(n):
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next
    current.next = current.next.next
    return dummy.next