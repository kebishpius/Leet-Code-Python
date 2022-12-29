class Solution(object):
    def findDisappearedNumbers(self, nums):
        new = {}
        ans = []
        for i in range(1, len(nums)+1):
            if i not in new:
                new[i] = 0
            if nums[i-1] in new:
                new[nums[i-1]] += 1
            else:
                new[nums[i-1]] = 1
        for j in new:
            if new[j] == 0:
                ans.append(j)
        return ans
