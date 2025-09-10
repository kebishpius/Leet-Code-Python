# Last updated: 9/10/2025, 12:58:25 AM
class Solution(object):
    def searchInsert(self, nums, target):
        if nums.count(target) == 1:
            return nums.index(target)
        elif nums.count(target) == 0:
            for i in range(len(nums)):
                if target < nums[i]:
                    nums.insert(i, target)
                    return nums.index(target)
                elif target > nums[len(nums)-1]:
                    return len(nums) 
                else:
                    pass
                    
        
        
        
        
        
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        