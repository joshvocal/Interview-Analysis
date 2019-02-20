# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    """
    Solution 1: Recursive
    Time: O(log n)
    Space: O(log n)
    """

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        head = self.helper(0, len(nums) - 1, nums)
        return head

    def helper(self, lo, hi, nums):
        if lo > hi:
            return None

        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(lo, mid - 1, nums)
        node.right = self.helper(mid + 1, hi, nums)
        return node

