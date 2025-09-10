# Last updated: 9/10/2025, 12:55:53 AM
class Solution(object):
    def findMiddleIndex(self, nums):
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            x = nums[0:i]
            y = nums[i+1:]
            if sum(y) == sum(x):
                return i
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        