class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def return_kth_to_last(self, head, k):
        slow = dummy = ListNode(0)
        fast = head
        dummy.next = head

        for i in range(k):
            if fast.next:
                fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow.val


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

def print_list(head):
    while head:
        print(head.val)
        head = head.next

print(Solution().return_kth_to_last(head, 6))
print(Solution().return_kth_to_last(head, 5))
print(Solution().return_kth_to_last(head, 4))
print(Solution().return_kth_to_last(head, 3))
print(Solution().return_kth_to_last(head, 2))
print(Solution().return_kth_to_last(head, 1))
print(Solution().return_kth_to_last(head, 0))


        
