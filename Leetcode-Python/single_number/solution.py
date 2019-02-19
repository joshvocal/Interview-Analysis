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


"""
Solution 2: Math
Time: O(n)
Space: O(1)
"""

class Solution2:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums)) - sum(nums)

