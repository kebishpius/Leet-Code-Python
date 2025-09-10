# Last updated: 9/10/2025, 12:56:42 AM
class Solution(object):
    def numIdenticalPairs(self, nums):
        good = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    good += 1
        return good
        """
        :type nums: List[int]
        :rtype: int
        """
        