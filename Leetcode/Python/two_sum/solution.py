'''
Solution 1: HashMap
Time: O(n)
Space: O(n)
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        
        for i in range(len(nums)):
            compliment = target - nums[i]
            
            if compliment in hash_map:
                return [nums[compliment], i]
            
            hash_map[nums[i]] = i
            
        return -1, -1
        