# Last updated: 9/10/2025, 12:56:02 AM
class Solution(object):
    def arraySign(self, nums):
        product = 1
        for i in range(len(nums)):
            product = product * nums[i]
        if product == 0:
            return 0
        if product > 0:
            return 1
        if product < 0:
            return -1
        
        """
        :type nums: List[int]
        :rtype: int
        """