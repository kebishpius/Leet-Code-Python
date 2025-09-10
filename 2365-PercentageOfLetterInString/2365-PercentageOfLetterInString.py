# Last updated: 9/10/2025, 12:55:29 AM
class Solution(object):
    def percentageLetter(self, s, letter):
        x = (s.count(letter) * 100 / len(s)) 
        return x
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        