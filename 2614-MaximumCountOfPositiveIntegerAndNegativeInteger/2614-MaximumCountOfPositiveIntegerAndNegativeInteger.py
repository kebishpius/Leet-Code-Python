# Last updated: 9/10/2025, 12:55:16 AM
class Solution(object):
    def maximumCount(self, nums):
        positive = 0
        negative = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                positive = positive + 1
            if nums[i] < 0:
                negative = negative + 1
        if negative > positive:
            return negative
        if positive > negative:
            return positive
        if negative == positive:
            return positive
        
        
        """
        :type nums: List[int]
        :rtype: int
        """