# Last updated: 9/10/2025, 12:57:50 AM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        Max = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter+=1
            else:
                if counter > Max:
                    Max = counter
                counter = 0
        if counter > Max:
            Max = counter
        return Max
        
        
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        