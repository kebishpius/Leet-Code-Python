class Solution(object):
    def repeatedNTimes(self, nums):
        for i in nums:
            if nums.count(i) == len(nums)/2:
                return i
        
