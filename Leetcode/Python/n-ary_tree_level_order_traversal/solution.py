'''
Solution 1: BFS
Time: O(n)
Space: O(n)
'''


class Solution:
    def levelOrder(self, root):
        res = []

        if not root:
            return res

        queue = [root]

        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.pop()
                level.append(curr.val)

                for child in curr.children:
                    queue.insert(0, child)

            res.append(level)

        return res
