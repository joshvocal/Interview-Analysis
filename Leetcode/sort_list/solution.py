class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Solution 1: Copy
Time: O(n*log n)
Space: O(n)
"""

class Solution:
    def sortList(self, head):

        copy = []

        if not head:
            return copy

        curr = head
        while curr:
            copy.append(curr.val)
            curr = curr.next

        copy.sort()

        head = ListNode(copy[0])
        dummy = head

        for i in range(1, len(copy)):
            head.next = ListNode(copy[i])
            head = head.next

        return dummy
