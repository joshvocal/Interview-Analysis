'''
Solution 1: Fast-Slow
Time: O(n)
Space: O(1)
'''


def removeKthNodeFromEnd(head, k):
    fast = head
    slow = head

    for i in range(k):
        fast = fast.next

    if not fast:
        head.value = head.next.value
        head.next = head.next.next
        return

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

