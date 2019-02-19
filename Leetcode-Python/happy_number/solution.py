"""
Solution 1:
Time: O()
Space: O()
"""

class Solution:
    def isHappy(self, n):
        s = set()
        while n not in s:
            if n == 1:
                return True
            s.add(n)
            n = self.get_sum_square(n)

        return False

    def get_sum_square(self, n):
        res = 0
        while n:
            temp = n % 10
            res += temp * temp
            n //= 10

        return res
