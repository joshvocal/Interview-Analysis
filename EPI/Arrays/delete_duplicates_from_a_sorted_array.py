class Solution:
    def delete_duplicates(self, nums):
        if not nums or len(nums) == 0:
            return nums

        pos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[pos - 1]:
                nums[pos] = nums[i]
                pos += 1

        return pos

nums = [2,3,5,7,7,13]
print(Solution().delete_duplicates(nums))

