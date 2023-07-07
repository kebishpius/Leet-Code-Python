class Solution(object):
    def firstPalindrome(self, words):
        for i in range(len(words)):
            checkpalindrome = words[i][::-1]
            if checkpalindrome == words[i]:
                return checkpalindrome
        return ""
