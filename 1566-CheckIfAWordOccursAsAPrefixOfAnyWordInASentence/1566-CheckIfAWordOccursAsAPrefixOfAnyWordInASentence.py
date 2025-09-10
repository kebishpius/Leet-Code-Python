# Last updated: 9/10/2025, 12:56:47 AM
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        ans = sentence.split()
        for i in range(len(ans)):
            if ans[i].find(searchWord) == 0:
                return i + 1
        return -1
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        