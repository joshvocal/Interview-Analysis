class Solution:

    """
    Solution 1: DFS
    Time: O(2^n)
    Space: O(2^n)
    """

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, [], nums, 0)
        return res

    def helper(self, res, temp, nums, choice_index):
        res.append(list(temp))

        for i in range(choice_index, len(nums)):
            temp.append(nums[i])
            self.helper(res, temp, nums, choice_index + 1)
            temp.pop()

