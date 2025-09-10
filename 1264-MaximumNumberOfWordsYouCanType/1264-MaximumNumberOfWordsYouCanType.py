# Last updated: 9/10/2025, 12:57:01 AM
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        x = text.split()
        check = 0
        for i in x:
            count = 0
            for j in brokenLetters:
                if j in i:
                    count += 1
            if count == 0:
                check += 1
        return check
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        