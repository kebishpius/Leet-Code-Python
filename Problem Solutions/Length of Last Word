class Solution(object):
    def lengthOfLastWord(self, s):
        y = s.rsplit(" ")
        x = list(dict.fromkeys(y))
        while y[-1] == '':
            y.pop(-1)
        return len(y[-1])
