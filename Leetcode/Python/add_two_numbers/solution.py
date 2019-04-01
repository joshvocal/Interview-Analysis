# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode
        l3 = dummy
        sum = 0

        while l1 or l2:
            sum //= 10

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            l3.next = ListNode(sum % 10)
            l3 = l3.next

        if sum // 10 == 1:
            l3.next = ListNode(1)

        return dummy.next
