# Last updated: 9/10/2025, 12:58:18 AM
class Solution(object):
    def singleNumber(self, nums):
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]
        
        """
        :type nums: List[int]
        :rtype: int
        """