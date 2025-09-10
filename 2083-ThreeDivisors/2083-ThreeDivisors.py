# Last updated: 9/10/2025, 12:55:55 AM
class Solution(object):
    def isThree(self, n):
        x=[]
        for i in range(1, n+1):
            if n % i == 0:
                x.append(i)
            else: 
                pass
        if len(x) == 3:
            return True
        else:
            return False
        
        
        
        
        
        """
        :type n: int
        :rtype: bool
        """
        