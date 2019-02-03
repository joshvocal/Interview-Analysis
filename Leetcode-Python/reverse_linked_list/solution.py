# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    """
    Solution 1: Iterative
    Time: O(n)
    Space: O(1)
    """

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        prev = None
        curr = head
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

