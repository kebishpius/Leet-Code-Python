# Last updated: 9/10/2025, 12:55:51 AM
class Solution(object):
    def countKDifference(self, nums, k):
        count = 0 
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    count+=1
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        