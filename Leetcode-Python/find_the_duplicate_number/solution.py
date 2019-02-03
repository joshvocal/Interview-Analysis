class Solution:

    """
    Solution 1: Math (Summation Formula)
    Time: O(n)
    Space: O(1)
    """

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        actualSum = sum(nums)
        realSum = n * (n + 1) // 2
        return actualSum - realSum
