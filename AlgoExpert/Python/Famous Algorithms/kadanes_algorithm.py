'''
Time: O(n)
Space: O(1)
'''

def kadanesAlgorithm(nums):
    maxSoFar = nums[0]
    maxEndingHere = nums[0]

    for i in range(1, len(nums)):
        maxEndingHere = max(nums[i], maxEndingHere + nums[i])
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxSoFar

