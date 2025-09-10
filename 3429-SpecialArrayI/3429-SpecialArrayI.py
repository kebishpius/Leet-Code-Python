# Last updated: 9/10/2025, 12:54:55 AM
class Solution(object):
    def isArraySpecial(self, nums):
        for i in range(len(nums)-1):
            if (nums[i+1] % 2) == (nums[i] % 2):
                return False
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        