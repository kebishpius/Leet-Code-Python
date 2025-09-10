# Last updated: 9/10/2025, 12:58:02 AM
class Solution(object):
    def reverseVowels(self, s):
        x = ''
        for letter in s:
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
                x = x + letter 
        vowels = x[::-1]
        vowels_count = 0
        res = ''
        for letter in s:
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
                res = res + vowels[vowels_count]
                vowels_count +=1
            else:
                res = res + letter
        return res     

        ""
        """
        :type s: str
        :rtype: str
        """