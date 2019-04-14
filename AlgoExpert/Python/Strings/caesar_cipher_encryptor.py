'''
Solution 1: ASCII
Time: O(n)
Space: O(n)
'''

def caesarCipherEncryptor(string, key):
    arr = list(string)

    for i, char in enumerate(string):
        arr[i] = chr((ord(char) + key - ord('a')) % 26 + ord('a'))

    return ''.join(arr)
