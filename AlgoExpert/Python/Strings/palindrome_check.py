'''
Solution 1: Two Pointers
Time: O(n)
Space: O(1)
'''


def isPalindrome(string):
    if not string or not len(string):
        return True

    lo = 0
    hi = len(string) - 1

    while lo < hi:
        if string[lo] != string[hi]:
            return False

        lo += 1; hi -= 1

    return True
