# Last updated: 9/10/2025, 12:55:22 AM
class Solution(object):
    def findMaxK(self, nums):
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] * -1 == nums[j]:
                    return nums[i] * -1
        return -1