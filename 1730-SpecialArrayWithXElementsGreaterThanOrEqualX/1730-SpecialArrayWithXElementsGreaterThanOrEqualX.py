# Last updated: 9/10/2025, 12:56:41 AM
class Solution(object):
    def specialArray(self, nums):
        x = 0
        count = 0
        while x <= max(nums):
            for i in nums:
                if x <= i:
                    count+=1
            if count == x:
                return x
            count = 0
            x += 1
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        