class Solution:

    """
    Solution 1: Math (Summation Formula)
    Time: O(n)
    Space: O(1)
    """

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        actualSum = sum(nums)
        realSum = n * (n + 1) // 2
        return realSum - actualSum
