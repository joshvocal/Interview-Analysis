'''
Solution 1: In-place
Time: O(n)
Space: O(1)
'''


class Solution:
    def reverseOnlyLetters(self, S):

        n = len(S)
        lo = 0
        hi = n - 1
        S = list(S)

        while lo < hi:
            while lo < hi and not S[lo].isalpha():
                lo += 1
            while lo < hi and not S[hi].isalpha():
                hi -= 1
            S[lo], S[hi] = S[hi], S[lo]
            lo += 1
            hi -= 1

        return S
            