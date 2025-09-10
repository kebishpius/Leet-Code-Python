# Last updated: 9/10/2025, 12:55:54 AM
class Solution(object):
    def isPrefixString(self, s, words):
        new = ""
        for i in words:
            new += i
            if new == s:
                return True
        return False
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        