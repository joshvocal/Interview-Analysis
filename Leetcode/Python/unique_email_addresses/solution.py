"""
Solution 1: Set
Time: O(n)
Space: O(n)
"""


class Solution:
    def numUniqueEmails(self, emails):
        if not emails or len(emails) == 0:
            return 0

        s = set()

        for email in emails:
            local = email.split('@')[0]
            domain = email.split('@')[1]

            newLocal = local.split('+')[0].replace('.', '')
            newDomain = domain.split('+')[0]

            s.add(newLocal + '@' + newDomain)

        return len(s)
