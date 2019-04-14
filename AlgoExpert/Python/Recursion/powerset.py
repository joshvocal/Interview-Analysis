'''
Solution 1: Backtracking
'''


def powerset(nums):
    res = []

    if not nums:
        return [[]]

    backtrack(res, [], 0, nums)
    return res

def backtrack(res, temp, choice_index, nums):
    res.append(list(temp))

    for i in range(choice_index, len(nums)):
        temp.append(nums[i])
        backtrack(res, temp, i + 1, nums)
        temp.pop()

