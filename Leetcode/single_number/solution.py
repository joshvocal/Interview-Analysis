"""
Solution 1: Set
Time: O(n)
Space: O(n)
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()

        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)

        for num in s:
            return num

