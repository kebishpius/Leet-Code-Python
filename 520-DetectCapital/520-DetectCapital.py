# Last updated: 9/10/2025, 12:57:52 AM
class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper() == True or word.islower() == True:
            return True
        if word[0].isupper() == True and word[1:].islower() == True:
            return True