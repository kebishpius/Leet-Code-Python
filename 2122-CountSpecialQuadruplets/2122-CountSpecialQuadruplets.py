# Last updated: 9/10/2025, 12:55:52 AM
class Solution(object):
    def countQuadruplets(self, nums):
        count = 0
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for g in range(k+1,len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[g]:
                            count+=1
        return count

        