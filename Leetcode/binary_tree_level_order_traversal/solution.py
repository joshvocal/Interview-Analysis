"""
Solution 1: BFS
Time: O(n)
Space: O(log n) == O(h)
"""

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        if not root:
            return res

        queue = [root]

        while queue:
            node_level = []
            for i in range(len(queue)):
                curr_node = queue.pop()
                node_level.append(curr_node.val)

                if curr_node.left:
                    queue.insert(0, curr_node.left)
                if curr_node.right:
                    queue.insert(0, curr_node.right)

            res.append(node_level)

        return res

"""
Solution 2: DFS
Time: O(n)
Space: O(log n) == O(h)
"""

class Solution2:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
         res = []
         self.dfs(res, root, 0)
         return res

    def dfs(self, res, root, depth):
        if not root:
            return None
        if len(res) == depth:
            res.append([])
        res[depth].append(root.val)
        self.dfs(res, root.left, depth + 1)
        self.dfs(res, root.right, depth + 1)






















