class Solution(object):
    def replaceDigits(self, s):
        res = ''
        for i in range(len(s)):
            if s[i].isnumeric() == True:
                x = ord(s[i-1])
                x = x + int(s[i])
                x = chr(x)
                res = res + x
            else:
                res = res + s[i]
        return res
