# Last updated: 9/10/2025, 12:56:37 AM
class Solution(object):
    def maximumWealth(self, accounts):
        ans = []
        for i in accounts:
            ans.append(sum(i))
        return max(ans)
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        