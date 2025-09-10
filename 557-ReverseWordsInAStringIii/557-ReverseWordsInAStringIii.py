# Last updated: 9/10/2025, 12:57:51 AM
class Solution(object):
    def reverseWords(self, s):
        x = s[::-1]
        y = x.split()
        final = ''
        for i in range(len(y)):
            final = y[i] + " " + final
        return final.rstrip()  

        
        """
        :type s: str
        :rtype: str
        """