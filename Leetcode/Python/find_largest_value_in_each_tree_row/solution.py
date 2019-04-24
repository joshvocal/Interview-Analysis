'''
Solution 1: BFS
Time: O(n)
Space: O(n)
'''


class Solution:
    def largestValues(self, root):
        res = []

        if not root:
            return res

        queue = [root]
        biggest = -float('inf')
        biggestSoFar = -float('inf')

        while queue:
            for i in range(len(queue)):
                curr = queue.pop()
                biggestSoFar = curr.val

                if curr.left:
                    queue.insert(0, curr.left)
                if curr.right:
                    queue.insert(0, curr.right)

                biggest = max(biggest, biggestSoFar)

            res.append(biggest)
            biggest = -float('inf')
            biggestSoFar = -float('inf')

        return res
