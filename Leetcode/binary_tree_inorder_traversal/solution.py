# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    """
    Solution 1: Iterative
    Time: O(n)
    Space: O(log n) Worst: O(n)
    """

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = root.pop()
            res.append(root.val)
            root = root.left

        return res

    """
    Solution 2: Recursive
    Time: O(n)
    Space: O(log n) Worst: O(n)
    """

    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        if root:
            res = res + self.inorderTraversal2(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal2(root.right)

        return res
