# Last updated: 9/10/2025, 12:57:16 AM
class Solution(object):
    def pivotIndex(self, nums):
        sumleft = [0]
        sumright = [0]
        for i in range(len(nums)):
            sumleft[0] = sum(nums[0:i])
            sumright[0] = sum(nums[i+1:])
            if sumright[0] == sumleft[0]:
                return i
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """