# Last updated: 9/10/2025, 12:57:09 AM
class Solution(object):
    def reverseOnlyLetters(self, s):
        alpha = ''
        alpha_count = 0
        res = ''
        for letter in s:
            if letter.isalpha():
                alpha += letter
        alpha = alpha[::-1]
        for letter in s:
            if letter.isalpha():
                res += alpha[alpha_count]
                alpha_count += 1
            else:
                res += letter
        return res



        
        """
        :type s: str
        :rtype: str
        """