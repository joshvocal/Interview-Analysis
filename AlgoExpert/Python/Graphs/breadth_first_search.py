class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, root):
        res = []

        if not self:
            return res

        q = [self]

        while q:
            curr_node = q.pop()
            res.append(curr_node.name)
            for child in curr_node.children:
                q.insert(0, child)

        return res
