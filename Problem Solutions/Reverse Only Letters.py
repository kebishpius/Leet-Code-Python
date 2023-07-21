class Solution(object):
    def reversePrefix(self, word, ch):
        alpha = ''
        alpha_count = 0
        res = ''
        for letter in :
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
