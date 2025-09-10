# Last updated: 9/10/2025, 12:54:52 AM
class Solution(object):
    def canAliceWin(self, nums):
        nums.sort()
        if len(nums) == 1:
            return True
        for i in range(len(nums)):
            if len(str(nums[i])) == 2:
                return sum(nums[0:i]) != sum(nums[i:])
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        