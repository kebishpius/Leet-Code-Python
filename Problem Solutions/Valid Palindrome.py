class Solution(object):
    def isPalindrome(self, s):
        new = ''
        for letter in s:
            if letter.isalpha() == True or letter.isnumeric() == True:
                new = new + letter
        lower_new = new.lower()
        if lower_new[::-1] == lower_new:
            return True
        return False
