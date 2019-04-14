'''
Solution 1: Stack
Time: O(n)
Space: O(n)
'''


def balancedBrackets(brackets):

    s = []

    for bracket in brackets:
        if bracket == '{':
            s.append('}')
        elif bracket = '(':
            s.append(')')
        elif bracket = '[':
            s.append(']')
        elif not s or s.pop() != bracket:
            return False

    # Check if the stack is not empty
    return not s

