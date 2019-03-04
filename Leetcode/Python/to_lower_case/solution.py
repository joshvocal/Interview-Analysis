'''
Solution 1: ASCII Values
Time: O(n)
Space: O(1)
'''


class Solution:
    def toLowerCase(self, str: str) -> str:
        
        str = list(str)
        
        for i in range(len(str)):
            if ord('A') <= ord(str[i]) <= ord('Z'):
                str[i] = chr(ord(str[i]) - ord('A') + ord('a'))
                
        return "".join(str)
        