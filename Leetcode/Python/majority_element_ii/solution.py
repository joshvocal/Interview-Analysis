class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        if not nums:
            return res

        candOne = nums[0]
        candTwo = nums[0]
        countOne = 0
        countTwo = 0

        for num in nums:
            if candOne == num:
                countOne += 1
            elif candTwo == num:
                countTwo += 1
            elif countOne == 0:
                candOne = num
                countOne = 1
            elif countTwo == 0:
                candTwo = num
                countTwo = 1
            else:
                countOne -= 1
                countTwo -= 1

        countOne = 0
        countTwo = 0

        for num in nums:
            if candOne == num:
                countOne += 1
            elif candTwo == num:
                countTwo += 1

        if countOne > len(nums) // 3:
            res.append(candOne)
        if countTwo > len(nums) // 3:
            res.append(candTwo)

        return res
