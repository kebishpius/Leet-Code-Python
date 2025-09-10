# Last updated: 9/10/2025, 12:56:42 AM
class Solution(object):
    def countOdds(self, low, high):
        if low % 2 == 0 and high % 2 == 0: 
            return (high-low)/2
        if low % 2 != 0 and high % 2 != 0: 
            return (high-low)//2 + 1
        if low % 2 != 0 and high % 2 == 0: 
            return (high-low)//2 + 1
        if low % 2 == 0 and high % 2 != 0: 
            return (high-low)//2 + 1
        
        
        """
        :type low: int
        :type high: int
        :rtype: int
        """