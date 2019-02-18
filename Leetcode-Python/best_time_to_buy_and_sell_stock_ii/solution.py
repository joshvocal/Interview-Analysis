"""
Solution 1: Iterative
Time: O(n)
Space: O(1)

Only add to your profit if the difference between prices is positive
"""

class Solution:
    def maxProfit(self, prices):
        profit = 0

        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])

        return profit