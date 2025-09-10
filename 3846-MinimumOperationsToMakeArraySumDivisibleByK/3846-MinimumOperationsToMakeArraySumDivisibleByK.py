# Last updated: 9/10/2025, 12:54:55 AM
class Solution(object):
    def minOperations(self, nums, k):
        x = sum(nums)
        count = 0
        while x % k != 0:
            x -= 1
            count+=1
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        