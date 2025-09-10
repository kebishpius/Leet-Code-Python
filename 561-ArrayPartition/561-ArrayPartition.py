# Last updated: 9/10/2025, 12:59:06 AM
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        total = 0
        for i in range(0,len(nums),2):
            total += nums[i]
        return total


        """
        :type nums: List[int]
        :rtype: int
        """
        