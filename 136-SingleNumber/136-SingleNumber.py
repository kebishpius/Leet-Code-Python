# Last updated: 9/10/2025, 12:58:18 AM
class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i) == 1:
                return i
            else:
                pass
        
        
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        