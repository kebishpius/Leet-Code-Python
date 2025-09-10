# Last updated: 9/10/2025, 12:55:54 AM
class Solution(object):
    def numOfStrings(self, patterns, word):
        x=[]
        for i in range(len(patterns)):
            if word.find(patterns[i]) != -1:
                x.append(patterns[i])
        
        return len(x)
        
        
        
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        