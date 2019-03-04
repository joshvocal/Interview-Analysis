'''
Solution 1: Brute Force
Time: O(n*m)
Space: O(1)
'''

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewels = 0
        
        if not S or len(S) == 0:
            return jewels
        
        for stone in S:
            for jewel in J:
                if jewel == stone:
                    jewels += 1
                    
        return jewels