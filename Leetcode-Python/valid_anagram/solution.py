class Solution:

    """
    Solution 1: HashMap
    Time: O(n)
    Space: O(n)
    """

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}

        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for char in t:
            if char in dic:
                dic[char] -= 1
                if dic[char] == 0:
                    del dic[char]
            else:
                return False

        return len(dic) == 0
