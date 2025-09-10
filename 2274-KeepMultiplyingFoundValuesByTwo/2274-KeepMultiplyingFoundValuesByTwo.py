# Last updated: 9/10/2025, 12:55:38 AM
class Solution(object):
    def findFinalValue(self, nums, original):
        nums.sort()
        for i in range(len(nums)):
            if original == nums[i]:
                original = original * 2
            
        return original