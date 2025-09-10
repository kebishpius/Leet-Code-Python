# Last updated: 9/10/2025, 12:55:38 AM
class Solution(object):
    def countElements(self, nums):
        count = 0
        for i in nums:
            if i != min(nums) and i != max(nums):
                count+=1
        return count

        """
        :type nums: List[int]
        :rtype: int
        """
        