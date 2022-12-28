class Solution(object):
    def maxProduct(self, nums):
        maxs = []
        if len(nums) == 2:
            return (nums[0] - 1) * (nums[1] -1)
        for i in range(2):
            maxs.append(max(nums))
            nums.remove(max(nums))
        return (maxs[0] - 1) * (maxs[1] -1)
