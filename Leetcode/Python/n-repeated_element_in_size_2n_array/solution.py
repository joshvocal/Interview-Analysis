'''
Solution 1: Set
Time: O(n)
Space: O(n)
'''


class Solution:
    def repeatedNTimes(self, A):
        
        s = set()
        
        for num in A:
            if num in s:
                return num
            s.add(num)
        

'''
Solution 2: Math
Time: O(n)
Space: O(1)
'''


class Solution2:
    def repeatedNTimes(self, A):
        
        for i in range(2, len(A)):
            if A[i] == A[i - 1] or A[i] == A[i - 2]:
                return A[i]
            
        return A[0]
        