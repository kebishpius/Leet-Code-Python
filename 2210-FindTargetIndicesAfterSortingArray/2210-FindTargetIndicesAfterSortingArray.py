# Last updated: 9/10/2025, 12:55:45 AM
class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        temp = []
        for i in range(len(nums)):
            if nums[i] == target:
                temp.append(i)
        return temp

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        