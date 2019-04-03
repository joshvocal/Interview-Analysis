"""
Solution 1:
Time: O(n)
Space: O(n)
"""


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = []
        count = 0

        for i in range(len(S) - 1, -1, -1):
            if S[i] == '-':
                continue

            if count % (K + 1) == K:
                res.append('-')
                count += 1

            res.append(S[i].upper())
            count += 1

        return ''.join(reversed(''.join(res)))
