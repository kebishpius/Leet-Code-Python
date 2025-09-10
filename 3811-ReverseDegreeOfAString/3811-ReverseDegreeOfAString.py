# Last updated: 9/10/2025, 12:54:53 AM
class Solution(object):
    def reverseDegree(self, s):
        ans = []
        for i in range(len(s)):
            ans.append((123-ord(s[i]))*(i+1))
        return sum(ans)
        """
        :type s: str
        :rtype: int
        """
        