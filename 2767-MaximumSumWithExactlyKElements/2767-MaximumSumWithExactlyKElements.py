# Last updated: 9/10/2025, 12:55:08 AM
class Solution(object):
    def maximizeSum(self, nums, k):
        ans = 0
        for i in range(k):
            ans += max(nums) + i
        return ans
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        