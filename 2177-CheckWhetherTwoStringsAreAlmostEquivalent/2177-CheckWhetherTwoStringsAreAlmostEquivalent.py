# Last updated: 9/10/2025, 12:55:48 AM
class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        for i in word1:
            if word1.count(i) - word2.count(i) > 3:
                return False
        for j in word2:
            if word2.count(j) - word1.count(j) > 3:
                return False
        return True
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        