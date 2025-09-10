# Last updated: 9/10/2025, 12:55:58 AM
class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
        """
        :type nums: List[int]
        :rtype: int
        """