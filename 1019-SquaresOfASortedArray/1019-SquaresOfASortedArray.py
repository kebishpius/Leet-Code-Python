# Last updated: 9/10/2025, 12:57:07 AM
class Solution(object):
    def sortedSquares(self, nums):
        squared_nums = []
        for i in nums:
            squared_nums.append(i*i)
        squared_nums.sort()
        return squared_nums
        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        