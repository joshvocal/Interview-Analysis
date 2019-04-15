def smallestDifference(A, B):
    A.sort()
    B.sort()

    a = 0
    b = 0

    smallestDiff = float('inf')
    res = [0, 0]

    while a < len(A) and b < len(B):

        i = A[a]
        j = B[b]

        if smallestDiff > abs(i - j):
            smallestDiff = min(smallestDiff, abs(i - j))
            res = [i, j]
        elif i > j:
            b += 1
        else:
            a += 1

    return res


