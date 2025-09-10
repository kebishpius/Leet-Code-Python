# Last updated: 9/10/2025, 12:55:33 AM
class Solution(object):
    def divideArray(self, nums):
        pairs = []
        for i in range(len(nums)):
            if nums.count(nums[i]) % 2 == 0:
                pairs.append(nums[i])
        if len(pairs) == len(nums):
            return True
        else:
            return False
        
        """
        :type nums: List[int]
        :rtype: bool
        """