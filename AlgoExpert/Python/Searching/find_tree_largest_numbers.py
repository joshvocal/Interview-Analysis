import heapq

'''
Time: O(nlogn)
Space: O(n)
'''

def findThreeLargestNumbers(nums):
    heapq.heapify(nums)

    while len(nums) > 3:
        heapq.heappop(nums)

    nums.sort()
    return nums
