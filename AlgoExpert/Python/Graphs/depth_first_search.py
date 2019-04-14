class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, nums):
        nums.append(self.name)
        for child in self.children:
            child.depthFirstSearch(nums)
        return nums
            


