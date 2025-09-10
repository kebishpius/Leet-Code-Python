# Last updated: 9/10/2025, 12:55:08 AM
class Solution(object):
    def sumOfMultiples(self, n):
        ans = 0
        for i in range(n+1):
            if i % 3 == 0:
                ans += i
            elif i % 5 == 0:
                ans += i
            elif i % 7 == 0:
                ans += i
        return ans
        """
        :type n: int
        :rtype: int
        """
        