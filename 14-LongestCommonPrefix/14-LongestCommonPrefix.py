# Last updated: 9/10/2025, 12:58:28 AM
class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort(key = len)
        n = len(strs)
        ans = ""
        for i in range(len(strs[0])):
            for j in range(1,n):
                if(strs[0][i] != strs[j][i]):
                    return ans
            ans += strs[0][i]
        return ans


        """
        :type strs: List[str]
        :rtype: str
        """
        