'''
Solution 1: Three Pointers
Time: O(n^2)
space: O(1)
'''

def threeNumberSum(nums, target):
    triplets = []

    if not nums or len(nums) < 3:
        return triplets

    nums.sort()

    for i in range(len(nums) - 2):
        lo = i + 1
        hi = len(nums) - 1

        while lo < hi:
			cs = nums[i] + nums[lo] + nums[hi]
            if cs == target:
                triplets.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
            elif cs > target:
                hi -= 1
            else:
                lo += 1

    return triplets
