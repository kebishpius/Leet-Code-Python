# Last updated: 9/10/2025, 12:54:59 AM
class Solution(object):
    def findWordsContaining(self, words, x):
        ans = []
        for i in range(len(words)):
            if words[i].find(x) != -1:
                ans.append(i)
        return ans
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        