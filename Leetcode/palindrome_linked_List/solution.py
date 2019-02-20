class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Solution 1: Temp Array
Time: O(n)
Space: O(n)
"""

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        n = len(nums)
        for i in range(n//2):
            if nums[i] != nums[n - 1 - i]:
                return False

        return True


"""
Solution 2: Reverse Half-Way
Time: O(n)
Space: O(1)
"""

class Solution2:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        if fast:
            slow = slow.next

        slow = self.reverse()
        fast = head

        while not slow:
            if fast.val != slow.val:
                return False

            fast = fast.next
            slow = slow.next

        return True

    def reverse(self, head):
        prev = None
        while head:
            curr = head.next
            head.next = prev
            prev = curr
            curr = next
        return prev
