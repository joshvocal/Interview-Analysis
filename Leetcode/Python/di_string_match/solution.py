'''
Solution 1: Two-Pointers
Time: O(n)
Space: O(1)
'''


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        res = []
        
        if not S or len(S) == 0:
            return res
        
        lo = 0
        hi = len(S) 
        
        for i in range(len(S)):
            if S[i] == "I":
                res.append(lo)
                lo += 1
            elif S[i] == "D":
                res.append(hi)
                hi -= 1
                
        res.append(lo)
        
        return res
         