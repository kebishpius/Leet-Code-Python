# Last updated: 9/10/2025, 12:55:01 AM
class Solution(object):
    def countPairs(self, nums, target):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        