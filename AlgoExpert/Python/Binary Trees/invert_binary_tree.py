'''
Solution 1: BFS
Time: O(n)
Space: O(n)
'''


def invertBinaryTree(root):
    if not root:
        return root

    q = [root]

    while q:
        curr_node = q.pop()
        curr_node.left, curr_node.right = curr_node.right, curr_node.left

        if curr_node.left:
            q.insert(0, curr_node.left)
        if curr_node.right:
            q.insert(0, curr_node.right)
