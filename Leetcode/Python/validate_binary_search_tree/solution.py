# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
Solution 1:
Time: O(n)
Space: O(log n)
'''


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        prev = None
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right
            
        return True
    