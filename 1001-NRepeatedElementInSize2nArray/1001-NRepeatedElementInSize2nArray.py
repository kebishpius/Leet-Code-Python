# Last updated: 9/10/2025, 12:57:08 AM
class Solution(object):
    def repeatedNTimes(self, nums):
        for i in nums:
            if nums.count(i) == len(nums)/2:
                return i
        
        """
        :type nums: List[int]
        :rtype: int
        """