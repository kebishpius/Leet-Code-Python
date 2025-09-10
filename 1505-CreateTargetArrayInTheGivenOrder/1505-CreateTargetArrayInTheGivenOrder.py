# Last updated: 9/10/2025, 12:56:50 AM
class Solution(object):
    def createTargetArray(self, nums, index):
        x = []
        for i in range(len(nums)):
            x.insert(index[i], nums[i])

        return x
        
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """