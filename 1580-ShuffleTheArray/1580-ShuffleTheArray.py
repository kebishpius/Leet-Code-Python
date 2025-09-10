# Last updated: 9/10/2025, 12:56:44 AM
class Solution(object):
    def shuffle(self, nums, n):
        x=[]
        for i in range(len(nums)-n):
            x.append(nums[i])
            x.append(nums[i+n])
        
        return x
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """