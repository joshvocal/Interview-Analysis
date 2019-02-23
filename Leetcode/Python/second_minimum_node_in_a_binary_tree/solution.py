# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    """
    Solution 1: BFS
    Time: O(n)
    Space: O(n)
    """

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        min = root.val
        secondMin = float('inf')

        while queue:
            for node in queue:
                curr_node = queue.pop()
                if min < curr_node.val < secondMin:
                    secondMin = curr_node.val

                if curr_node.left:
                    queue.insert(0, curr_node.left)
                if curr_node.right:
                    queue.insert(0, curr_node.right)

        return -1 if secondMin == float('inf') else secondMin


    """
    Solution 2: In-order Traversal Iterative
    Time: O(n)
    Space: O(log n)
    """

    def findSecondMinimumValue2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        stack = []
        minimum = root.val
        secondMin = float('inf')

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if minimum < root.val < secondMin:
                secondMin = root.val
            root = root.right

        return -1 if float('inf') == secondMin else secondMin
