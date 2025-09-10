# Last updated: 9/10/2025, 12:54:57 AM
class Solution(object):
    def scoreOfString(self, s):
        ans = []
        for i in range(len(s)-1):
            ans.append(abs(ord(s[i]) - ord(s[i+1])))
        return sum(ans)

        """
        :type s: str
        :rtype: int
        """
        