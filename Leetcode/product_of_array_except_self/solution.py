"""
Solution 1:
Time: O(2*n)
Space: O(1)
"""

class Solution:
    def productExceptSelf(self, nums):

        output = []
        n = len(nums)

        prod = 1
        for i in range(n):
            output.append(prod)
            prod = prod * nums[i]

        prod = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * prod
            prod = prod * nums[i]

        return prod
