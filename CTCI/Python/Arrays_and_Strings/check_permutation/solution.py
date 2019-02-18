"""
Solution 1: Array
Time: O(2*n)
Space: O(1)
"""

class Solution:
    def check_permutation(self, str1, str2): 
        if not str1 or not str2 or len(str1) != len(str2):
            return False

        freq_table = [0 for i in range(26)]

        for char in str1:
            freq_table[ord(char) - ord('a')] += 1

        for char in str2:
            freq_table[ord(char) - ord('a')] -= 1
            if freq_table[ord(char) - ord('a')] < 0:
                return False

        return True


"""
Solution 2: Sort
Time: O(n*log n)
Space: O(1)
"""

class Solution2:
    def check_permutation(self, str1, str2): 
        if not str1 or not str2 or len(str1) != len(str2):
            return False

        str1 = "".join(sorted(str1))
        str2 = "".join(sorted(str2))

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False

        return True



str1 = "hello"
str2 = "hello"
print(Solution().check_permutation(str1, str2))
print(Solution2().check_permutation(str1, str2))
