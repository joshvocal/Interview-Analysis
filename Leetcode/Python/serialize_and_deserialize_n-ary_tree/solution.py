# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Codec:
    def serializeHelper(self, node, arr):
        if node:
            arr.append(str(node.val))
            arr.append(str(len(node.children)))
            for child in node.children:
                self.serializeHelper(child, arr)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []
        self.serializeHelper(root, res)
        return ','.join(res)

    def deserializeHelper(self, q):
        root = Node(int(q.pop(0)), [])
        size = int(q.pop(0))

        for _ in range(size):
            root.children.append(self.deserializeHelper(q))

        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        queue = data.split(',')
        return self.deserializeHelper(queue)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
