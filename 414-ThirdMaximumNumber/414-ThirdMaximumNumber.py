# Last updated: 9/10/2025, 12:57:55 AM
class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        nums.sort()
        return nums[len(nums)-3]
        """
        :type nums: List[int]
        :rtype: int
        """
        