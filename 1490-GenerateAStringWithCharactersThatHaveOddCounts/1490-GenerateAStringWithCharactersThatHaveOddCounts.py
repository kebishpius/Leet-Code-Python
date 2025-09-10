# Last updated: 9/10/2025, 12:56:51 AM
class Solution(object):
    def generateTheString(self, n):
        z=""
        y=n-1
        c= n-2
        if n == 1:
            return 'x'
        else:
            pass
        if n % 2 == 0:
            for i in range(n-1):
                z= y * 'x'
            return z + 'y'
        else:
            pass
        if n % 2 > 0:
            for i in range(n-2):
                z= c * 'x'
            return z + 'y' + 'z'
        else:
            pass
        
        
        
        
        
        
        
        
        
        """
        :type n: int
        :rtype: str
        """
        