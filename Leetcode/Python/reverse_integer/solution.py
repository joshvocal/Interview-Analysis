class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0
        x = abs(x)
        reverse = 0
        while x != 0:
            reverse = reverse * 10 + x % 10
            x //= 10
            
        INT_MAX_32 = 2**31 - 1
        if reverse > INT_MAX_32:
            return 0
        elif is_negative:
            return -reverse
        else:
            return reverse