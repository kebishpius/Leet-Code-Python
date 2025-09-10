# Last updated: 9/10/2025, 12:56:48 AM
class Solution(object):
    def kLengthApart(self, nums, k):
        if nums.count(1) == 0:
            return True
        x = nums.index(1)
        count = 0
        for i in range(x+1, len(nums)):
            if nums[i] == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1
        return True
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        