# Last updated: 9/10/2025, 12:55:46 AM
class Solution(object):
    def maxSubsequence(self, nums, k):
        h = 0
        for i in range(len(nums)-k):
            h = min(nums)
            nums.pop(nums.index(h))
        return nums
            
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """