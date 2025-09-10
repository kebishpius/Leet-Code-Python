# Last updated: 9/10/2025, 12:55:19 AM
class Solution(object):
    def isCircularSentence(self, sentence):
        x = sentence.split()
        if len(x) == 1:
            return x[0][0] == x[0][-1]
        for i in range(len(x)-1):
            if x[i][-1] != x[i+1][0]:
                return False
        if x[-1][-1] == x[0][0]:
            return True
        return False
            

        """
        :type sentence: str
        :rtype: bool
        """
        