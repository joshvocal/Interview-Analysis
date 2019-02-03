class Solution:

    """
    Solution 1: Iterative
    Time: O(n)
    Space: O(1)
    """

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        size = len(nums)
        
        for i in range(size):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                zero_index += 1
                
        for i in range(zero_index, size):
            nums[i] = 0
