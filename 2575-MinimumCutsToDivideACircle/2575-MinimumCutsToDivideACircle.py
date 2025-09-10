# Last updated: 9/10/2025, 12:55:18 AM
class Solution(object):
    def numberOfCuts(self, n):
        if n == 1:
            return 0
        if n % 2 == 0:
            return n / 2
        return n
        """
        :type n: int
        :rtype: int
        """
        