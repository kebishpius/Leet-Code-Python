class Solution(object):
    def reverseWords(self, s):
        x = s.strip()
        y = x.split()
        y.reverse()
        print(y)
        ans = ' '
        for i in range(len(y)):
            ans = ans + ' ' + y[i]
        return ans.strip()
