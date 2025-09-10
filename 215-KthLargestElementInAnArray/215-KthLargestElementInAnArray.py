# Last updated: 9/10/2025, 12:58:12 AM
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums)-k]
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """