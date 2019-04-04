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


"""
Solution 2:
Time: O(n^2)
Space: O(n)
"""


class Solution2:
    def productExceptSelf(self, nums):

        res = [1 for num in nums]

        if not nums or len(nums) == 0:
            return res

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    res[i] *= nums[j]

        return res
