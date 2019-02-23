class Solution:

    """
    Solution 1: Stack
    Time: O(n)
    Space: O(n)
    """

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif not stack or stack.pop() != char:
                return False

        return len(stack) == 0


