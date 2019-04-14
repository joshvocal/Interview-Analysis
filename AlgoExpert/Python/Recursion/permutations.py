def getPermutations(nums):
    res = []

    if not nums:
        return nums

    backtrack(res, [], nums)
    return res

def backtrack(res, temp, nums):
    if len(temp) == len(nums):
        res.append(list(temp))
    else:
        for num in nums:
            if num not in temp:
                temp.append(num)
                backtrack(res, temp, nums)
                temp.pop()

print(permutations([1,2,3]))
