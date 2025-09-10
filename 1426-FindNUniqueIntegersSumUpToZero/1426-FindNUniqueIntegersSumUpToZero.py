# Last updated: 9/10/2025, 12:56:57 AM
class Solution(object):
    def sumZero(self, n):
        ans = []
        for i in range(1,n/2 + 1):
            ans.append(i)
            ans.append(-i)
        if n % 2 == 1:
            ans.append(0)
        return ans

        """
        :type n: int
        :rtype: List[int]
        """
        