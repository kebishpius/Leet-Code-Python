# Last updated: 9/10/2025, 12:58:30 AM
class Solution(object):
    def twoSum(self, nums, target):
        x = -452
        ans = []
        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """