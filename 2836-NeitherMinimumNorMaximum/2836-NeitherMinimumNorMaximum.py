# Last updated: 9/10/2025, 12:55:04 AM
class Solution(object):
    def findNonMinOrMax(self, nums):
        if len(nums) <= 2:
            return -1
        nums.remove(max(nums))
        nums.remove(min(nums))
        return nums[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        