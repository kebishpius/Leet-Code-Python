class Solution(object):
    def dominantIndex(self, nums):
        x = max(nums)
        y = nums.index(max(nums))
        nums.remove(max(nums))
        if x / 2 >= max(nums):
            return y
        else:
            return -1
