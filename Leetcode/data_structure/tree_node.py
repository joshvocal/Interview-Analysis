# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def array_to_tree(self, arr, root, i):
        if i < len(arr):
            temp = TreeNode(arr[i])
            root = temp

            root.left = self.array_to_tree(arr, root.left, 2 * i + 1)
            root.right = self.array_to_tree(arr, root.right, 2 * i + 2)

        return root

    def print_tree_in_order(self, root):
        if root:
            self.print_tree_in_order(root.left)
            print(root.val)
            self.print_tree_in_order(root.right)

