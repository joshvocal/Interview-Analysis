class Solution:

    """
    Solution 1: HashMap
    Time: O(n)
    Space: O(n)
    """
    
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}

        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i

        return -1

