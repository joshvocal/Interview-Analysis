"""
Solution 1: Iterative
Time: O(n)
Space: O(1)
"""


class Solution:
    def findPeakElement(self, nums):

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len(nums) - 1


"""
Solution 2: Binary Search
Time: O(log n)
Space: O(1)
"""


class Solution2:
    def findPeakElement(self, nums):

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1

        return lo

