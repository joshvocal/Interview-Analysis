"""
Solution 1: Recursive
Time: O(2^n)
Space: O(1)
"""

class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """

        if N <= 1:
            return N
        else:
            return self.fib(N - 1) + self.fib(N - 2)


"""
Solution 2: DP
Time: O(n)
Space: O(n)
"""

class Solution2:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """

        dp = [0] * (N + 2)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[N]

