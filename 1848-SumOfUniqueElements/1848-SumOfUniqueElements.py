# Last updated: 9/10/2025, 12:59:04 AM
class Solution(object):
    def sumOfUnique(self, nums):
        x=[]
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                x.append(nums[i])
        if len(x) == 0:
            return 0
        return sum(x)
        
        
        
        
        
        
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        