# Last updated: 9/10/2025, 12:56:40 AM
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        word3 = ''
        word4 = ''
        for i in range(len(word1)):
            word3 = word3 + word1[i]
        for j in range(len(word2)):
            word4 = word4 + word2[j]
        if word4 == word3:
            return True
        else:
            return False
        
        
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """