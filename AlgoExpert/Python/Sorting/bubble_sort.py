'''
Time: O(n^2)
Space: O(1)
'''

def bubbleSort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1] , nums[j]

    return nums
