"""
Solution 1: Iterative
Time: O(n)
Space: O(1)
"""

class Solution:
    def maxProfit(self, prices):

        maxx = 0
        minn = float('inf')

        for price in prices:
            if price < minn:
                minn = price
            else:
                maxx = max(maxx, price - minn)

        return maxx