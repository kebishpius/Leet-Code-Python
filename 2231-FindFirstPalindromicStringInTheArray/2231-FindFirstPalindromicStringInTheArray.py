# Last updated: 9/10/2025, 12:55:43 AM
class Solution(object):
    def firstPalindrome(self, words):
        for i in range(len(words)):
            checkpalindrome = words[i][::-1]
            if checkpalindrome == words[i]:
                return checkpalindrome
        return ""
        
        """
        :type words: List[str]
        :rtype: str
        """