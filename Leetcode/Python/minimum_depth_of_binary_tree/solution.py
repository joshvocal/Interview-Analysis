'''
Solution 1: BFS
Time: O(n)
Space: O(n)
'''


class Solution:
    def minDepth(self, root):

        minDepth = 1

        if not root:
            return 0

        queue = [root]

        while queue:
            for i in range(len(queue)):
                curr = queue.pop()
                if not curr.left and not curr.right:
                    return minDepth

                if curr.left:
                    queue.insert(0, curr.left)
                if curr.right:
                    queue.insert(0, curr.right)

            minDepth += 1

        return minDepth
