class Solution:

    """
    Solution 1: Set
    Time: O(n)
    Space: O(n)
    """

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()

        for num in nums:
            if num in s:
                return True
            s.add(num)

        return False

