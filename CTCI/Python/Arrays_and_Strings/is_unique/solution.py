"""
Solution 1: Set
Time: O(n)
Space: O(n)
"""

class Solution:
    def is_unique(self, str):
        s = set()

        for char in str:
            if char in s:
                return False
            s.add(char)

        return True


"""
Solution 2: Array
Time: O(n)
Space: O(1)
"""

class Solution2:
    def is_unique(self, str):
        freq_table = [0 for i in range(26)]

        for char in str:
            freq_table[ord(char) - ord('a')] += 1
            if freq_table[ord(char) - ord('a')] >  1:
                return False

        return True



print(Solution().is_unique("Helo"))
print(Solution2().is_unique("Helo"))

print(Solution().is_unique(""))
print(Solution2().is_unique(""))

print(Solution().is_unique("ll"))
print(Solution2().is_unique("ll"))


        
        
            
