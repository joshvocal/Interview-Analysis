# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Solution 1: Iterative
Time: O(n)
Space: O(1)
"""


class Solution:

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


"""
Solution 2: Recursive
Time: O(n)
Space: O(n)
"""


class Solution2:

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head, None)

    def helper(self, curr, prev):
        if not curr:
            return prev

        next = curr.next
        curr.next = prev
        return self.helper(next, curr)
