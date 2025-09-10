# Last updated: 9/10/2025, 12:58:06 AM
class Solution(object):
    def singleNumber(self, nums):
        if len(nums) < 3: 
            return nums
        ans = []
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                ans.append(nums[i])
        return ans

        """
        :type nums: List[int]
        :rtype: List[int]
        """