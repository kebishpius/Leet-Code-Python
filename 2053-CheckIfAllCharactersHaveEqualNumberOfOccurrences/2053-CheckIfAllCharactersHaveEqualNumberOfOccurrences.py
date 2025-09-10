# Last updated: 9/10/2025, 12:55:56 AM
class Solution(object):
    def areOccurrencesEqual(self, s):
        count = s.count(s[0])
        for i in s[1:]:
            if s.count(i) != count:
                return False
        return True
        """
        :type s: str
        :rtype: bool
        """
        