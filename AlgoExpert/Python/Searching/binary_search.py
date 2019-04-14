'''
Time: O(logn)
Space: O(1)
'''


def binarySearch(nums, target):
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

    return - 1
