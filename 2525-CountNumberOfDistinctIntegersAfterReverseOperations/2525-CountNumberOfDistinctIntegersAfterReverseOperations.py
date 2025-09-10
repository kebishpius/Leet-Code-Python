# Last updated: 9/10/2025, 12:55:22 AM
class Solution(object):
    def countDistinctIntegers(self, nums):
        y = len(nums)
        for i in range(y):
            x = str(nums[i])
            nums.append(int(x[::-1]))
        return len(list(set(nums)))
        
        """
        :type nums: List[int]
        :rtype: int
        """