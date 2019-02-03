class Solution:
    """
    Solution 1: DFS
    Time: O(n)
    Space: O(n!)
    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(res, [], nums)
        return res

    def backtrack(self, res, tmpList, nums):
        if len(tmpList) == len(nums):
            res.append(list(tmpList))
        else:
            for num in nums:
                if num not in tmpList:
                    tmpList.append(num)
                    self.backtrack(res, tmpList, nums)
                    tmpList.remove(tmpList[-1])

    """
    Solution 1: BFS
    Time: O(n)
    Space: O(n!)
    """

    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]

        while len(res[-1]) < len(nums):
            temp = res.pop()
            for num in nums:
                if num not in temp:
                    inner = list(temp)
                    inner.insert(0, num)
                    res.insert(0, inner)

        return res

