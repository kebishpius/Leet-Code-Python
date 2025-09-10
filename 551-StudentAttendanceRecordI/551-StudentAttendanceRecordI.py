# Last updated: 9/10/2025, 12:57:52 AM
class Solution(object):
    def checkRecord(self, s):
        if s.count('A') < 2 and s.find('LLL') == -1 :
            return True
        return False
        """
        :type s: str
        :rtype: bool
        """