# Last updated: 9/10/2025, 12:56:40 AM
class Solution(object):
    def restoreString(self, s, indices):
        ans = list(s)
        count = 0
        for i in indices:
            ans[i] = s[count]
            count += 1
        return "".join(ans)

        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        