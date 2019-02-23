class Solution:

    """
    Solution 1: DFS (Backtracking)
    Time:
    Space: O(2 * n) = O(n)
    """

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        self.backtrack(res, "", 0, 0, n)
        return res

    def backtrack(self, res, temp, opening, closing, n):
        if len(temp) == (2 * n):
            res.append(temp)
        else:
            if opening < n:
                self.backtrack(res, temp + "(", opening + 1, closing, n)
            if closing < opening:
                self.backtrack(res, temp + ")", opening, closing + 1, n)

