# Last updated: 9/10/2025, 12:56:02 AM
class Solution(object):
    def truncateSentence(self, s, k):
        s1 = s.rsplit()
        s2 = ''
        for i in range(k):
            s2 = s2 + ' '+ s1[i]
        return s2.strip()

        
        """
        :type s: str
        :type k: int
        :rtype: str
        """