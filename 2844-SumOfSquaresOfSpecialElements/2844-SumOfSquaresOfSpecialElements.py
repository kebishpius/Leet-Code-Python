# Last updated: 9/10/2025, 12:55:03 AM
class Solution(object):
    def sumOfSquares(self, nums):
        ans = 0
        for i in range(len(nums)):
            if len(nums) % (i+1) == 0:
                ans += (nums[i] * nums[i])
        return ans


        """
        :type nums: List[int]
        :rtype: int
        """
        