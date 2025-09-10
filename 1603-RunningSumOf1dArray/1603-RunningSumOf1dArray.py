# Last updated: 9/10/2025, 12:56:43 AM
class Solution(object):
    def runningSum(self, nums):
        sums = 0
        storesums = []
        for i in range(len(nums)):
            sums = nums[i] + sums
            storesums.append(sums)
        return storesums
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """