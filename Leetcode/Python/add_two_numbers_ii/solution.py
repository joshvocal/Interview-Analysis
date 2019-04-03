"""
Solution 1: Stacks
Time: O(m)
Space: O(m)
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        sum = 0
        head = ListNode(0)

        while s1 or s2:
            if s1:
                sum += s1.pop()
            if s2:
                sum += s2.pop()

            head.val = sum % 10
            tail = ListNode(sum // 10)
            tail.next = head
            head = tail
            sum /= 10

        return head.next if head.val == 0 else head
