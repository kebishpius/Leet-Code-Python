# Last updated: 9/10/2025, 12:58:23 AM
class Solution(object):
    def lengthOfLastWord(self, s):
        y = s.rsplit(" ")
        x = list(dict.fromkeys(y))
        while y[-1] == '':
            y.pop(-1)
        return len(y[-1])
        
        """
        :type s: str
        :rtype: int
        """