# Last updated: 9/10/2025, 12:55:02 AM
class Solution(object):
    def isAcronym(self, words, s):
        if len(s) != len(words):
            return False
        for i in range(len(words)):
            if (words[i])[0] != s[i]:
                return False
        return True
        
        
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        