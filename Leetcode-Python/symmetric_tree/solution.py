class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Solution 1: Recursion
Time: O(n)
Space: O(log n)
"""

class Solution:
    def isSymmetric(self, root):
        return not root or self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left or not right:
            return left == right
        elif left.val != right.val:
            return False

        outer = self.helper(left.left, right.right)
        inner = self.helper(left.right, right.left)

        return outer and inner
