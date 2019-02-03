"""
Solution 1: For-loop
Time: O(n)
Space: O(1)
"""

class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """

        if not s or len(s) == 0:
            return s

        arr = list(s)
        length = len(s)

        for i in range(length // 2):
            temp = arr[i]
            arr[i] = arr[length - 1 - i]
            arr[length - 1 - i] = temp

        return ''.join(arr)


