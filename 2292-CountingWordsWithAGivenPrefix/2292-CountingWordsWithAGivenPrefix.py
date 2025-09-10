# Last updated: 9/10/2025, 12:55:35 AM
class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
        for i in words:
            if i.find(pref) == 0:
                count += 1
        return count
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        