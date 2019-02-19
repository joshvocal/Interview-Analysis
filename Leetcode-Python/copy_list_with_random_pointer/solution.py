class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


"""
Solution 1: HashMap
Time: O(n)
Space: O(n)
"""


class Solution:
    def copyRandomList(self, head):

        dic = {}
        m = n = head

        while m:
            dic[m] = RandomListNode(m.label)
            m = m.next

        while n:
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next

        return dic[head]
