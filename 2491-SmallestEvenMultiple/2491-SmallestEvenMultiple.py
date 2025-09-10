# Last updated: 9/10/2025, 12:55:23 AM
class Solution(object):
    def smallestEvenMultiple(self, n):
        if n == 1:
            return 2
        if n % 2 == 0:
            return n
        for i in range(1, n+1):
            for j in range(n+1):
                if 2 * j == n * i:
                    return 2 * j

        
        
        """
        :type n: int
        :rtype: int
        """