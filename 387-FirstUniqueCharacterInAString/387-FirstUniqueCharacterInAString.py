# Last updated: 9/10/2025, 12:57:57 AM
class Solution(object):
    def firstUniqChar(self, s):
        for i in s:
            if s.count(i) == 1:
                x = s.find(i)
                return x
        return -1
        
        """
        :type s: str
        :rtype: int
        """