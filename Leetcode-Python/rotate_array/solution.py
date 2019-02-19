"""
Solution 1: Reverse
Time: O(n)
Space: O(1)
"""


class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, lo, hi):
        while lo < hi:
            temp = nums[lo]
            nums[lo] = nums[hi]
            nums[hi] = temp
            lo += 1
            hi += 1

"""
Solution 2: Brute Force
Time: O(n*k)
Space: O(1)
"""


class Solution2:
    def rotate(self, nums, k):
        n = len(nums)

        for i in range(k):
            prev = nums[n - 1]
            for j in range(n):
                temp = nums[j]
                nums[j] = prev
                prev = temp
