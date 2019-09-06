class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        res = []

        if not root:
            return res

        q = [root]

        while q:
            level = []
            for i in range(len(q)):
                curr = q.pop(0)
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.insert(0, level)

        return res
