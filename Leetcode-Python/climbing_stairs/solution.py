class Solution:

    """
    Solution 1: DP
    Time: O(n)
    Space: O(n)
    """

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 2)

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]
