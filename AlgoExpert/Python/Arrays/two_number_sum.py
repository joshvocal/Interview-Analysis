'''
Solution 1: HashMap
Time: O(n)
Space: O(n)
'''


def twoNumberSum(arr, target):
    s = set()

    for num in arr:
        num_needed = target - num
        if num_needed in s:
            return sorted([num_needed, num])

        s.add(num)

    return []


'''
Solution 2: Two Pointers
Time: O(nlogn)
Space: O(1)
'''

def twoNumberSum2(arr, target):
	arr.sort()

	lo = 0
	hi = len(arr) - 1

	while lo < hi:
		left = arr[lo]
		right = arr[hi]
		cs = left + right
		if cs == target:
			return [left, right]
		elif cs > target:
			hi -= 1
		else:
			lo += 1
	return []
