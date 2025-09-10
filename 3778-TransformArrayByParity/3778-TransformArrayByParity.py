# Last updated: 9/10/2025, 12:54:54 AM
class Solution(object):
    def transformArray(self, nums):
        ans = []
        for i in nums:
            if i % 2 == 0:
                ans.append(0)
            else:
                ans.append(1)
        ans.sort()
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        