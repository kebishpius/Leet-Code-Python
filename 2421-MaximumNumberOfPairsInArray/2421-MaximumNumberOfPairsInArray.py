# Last updated: 9/10/2025, 12:55:26 AM
class Solution(object):
    def numberOfPairs(self, nums):
        pairs = 0
        left = 0
        for i in range(101):
            if nums.count(i) > 1:
                pairs += nums.count(i) / 2
            if nums.count(i) % 2 != 0:
                left += 1
        if pairs == 0:
            left = len(nums)
        return [pairs,left]
                


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        