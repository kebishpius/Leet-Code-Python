# Last updated: 9/10/2025, 12:56:56 AM
class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1,n+1):
            a = i
            b = n-i
            if a + b == n:
                if "0" in str(a) or "0" in str(b):
                    pass
                else:
                    return [a,b]
        """
        :type n: int
        :rtype: List[int]
        """
        