'''
Solution 1: Extra Space
Time: O(n)
Space: O(n)
'''


class Solution:
    def sortArrayByParity(self, A):

        res = [0 for num in A]
        lo = 0
        hi = len(A) - 1

        for i in range(len(A)):
            if A[i] % 2 == 0:
                res[lo] = A[i]
                lo += 1
            else: 
                res[hi] = A[i]
                hi -= 1

        return res


'''
Solution 2: Extra Space
Time: O(n)
Space: O(1)
'''


class Solution2:
    def sortArrayByParity(self, A):
        
        i = 0
        
        for j in range(len(A)):
            if A[j] % 2 == 0:
                A[j], A[i] = A[i], A[j]
                i += 1
                
        return A