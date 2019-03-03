# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
Solution 1: Iterative In-order
Time: O(n)
Space: O(log n)
'''


class Solution:
    def increasingBST(self, root):
        
        stack = []
        dummy = TreeNode(0)
        prev = dummy
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            root.left = None
            prev.right = root
            prev = root
            root = root.right
            
        return dummy.right
            