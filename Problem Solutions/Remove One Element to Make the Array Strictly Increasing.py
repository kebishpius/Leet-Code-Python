class Solution(object):
    def canBeIncreasing(self, nums):
        for i in range(len(nums)):
            count = 0
            x = nums[0:i] + nums[i+1:]
            for j in range(1,len(x)):
                if x[j-1] < x[j]:
                    count += 1
            if count == len(x) - 1:
                return True
        return False
