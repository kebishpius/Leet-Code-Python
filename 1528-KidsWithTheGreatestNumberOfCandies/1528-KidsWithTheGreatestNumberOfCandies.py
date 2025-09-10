# Last updated: 9/10/2025, 12:56:49 AM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        T_or_F = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                T_or_F.append(True)
            else:
                T_or_F.append(False)
        return T_or_F
                
        
        
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """