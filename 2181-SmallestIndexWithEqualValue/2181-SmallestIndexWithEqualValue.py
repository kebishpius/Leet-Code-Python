# Last updated: 9/10/2025, 12:55:47 AM
class Solution(object):
    def smallestEqual(self, nums):
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        