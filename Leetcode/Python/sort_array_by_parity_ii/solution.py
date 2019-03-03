'''
Solution 1: Two-Pointers
Time: O(n)
Space: O(1)
'''


class Solution:
    def sortArrayByParityII(self, A):
 
        if not A or len(A) == 0:
            return A

        even = 0
        odd = 1
        n = len(A)

        while even < n and odd < n:
            while even < n and A[even] % 2 == 0:
                even += 2
            while odd < n and A[odd] % 2 == 1:
                odd += 2
            if even < n and odd < n:
                A[even], A[odd] = A[odd], A[even]

        return A


'''
Solution 2: Extra Array
Time: O(n)
Space: O(n)
'''

class Solution2:
    def sortArrayByParityII(self, A):
 
        if not A or len(A) == 0:
            return A

        even = 0
        odd = 1
        n = len(A)
        res = [0 for num in A]

        for num in A:
            if num % 2 == 0:
                res[even] = num
                if even + 2 <= n:
                    even += 2
            else:
                res[odd] = num
                if odd + 2 <= n:
                    odd += 2

        return res
