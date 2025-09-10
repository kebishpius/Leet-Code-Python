# Last updated: 9/10/2025, 12:55:10 AM
class Solution(object):
    def findTheArrayConcVal(self, nums):
        ans = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)/2):
            x = str(nums[i])
            y = str(nums[len(nums)-1-i])
            ans += int(x+y)
        if len(nums) % 2 == 1:
            return ans + nums[len(nums)/2]
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        