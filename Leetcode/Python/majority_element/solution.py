class Solution:

    """
    Solution 1: Boyer-Moore
    Time: O(n)
    Space: O(1)
    """

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        count = 0

        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate = num
            else:
                count -= 1

        return candidate


