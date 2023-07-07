class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans
