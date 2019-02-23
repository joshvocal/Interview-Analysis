"""
Solution 1: Two Pointer
Time: O(n)
Space: O(1)
"""

class Solution:
    def isPalindrome(self, s):
        stripped = "".join(char for char in s if char.isalnum()).lower()
        n = len(stripped)

        for i in range(n // 2):
            if stripped[i] != stripped[n - 1 - i]:
                return False

        return True
