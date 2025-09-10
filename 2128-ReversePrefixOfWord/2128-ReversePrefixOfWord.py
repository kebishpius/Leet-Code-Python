# Last updated: 9/10/2025, 12:55:50 AM
class Solution(object):
    def reversePrefix(self, word, ch):
        for i in range(len(word)):
            if word[i] == ch:
                x = word[0:i+1]
                x = x[::-1]
                return x + word[i+1:]
        return word
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        