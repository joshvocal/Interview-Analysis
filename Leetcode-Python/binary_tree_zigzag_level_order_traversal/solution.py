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

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        if not root:
            return res

        queue = [root]

        while queue:
            nodes_in_level = []
            for i in range(len(queue)):
                curr_node = queue.pop()
                if len(res) % 2 != 0:
                    nodes_in_level.insert(0, curr_node.val)
                else:
                    nodes_in_level.append(curr_node.val)
                if curr_node.left:
                    queue.insert(0, curr_node.left)
                if curr_node.right:
                    queue.insert(0, curr_node.right)
            res.append(nodes_in_level)

        return res