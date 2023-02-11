class Solution(object):
    def findGCD(self, nums):
        maxnum = max(nums)
        minnum = min(nums)
        ans = 0
        for i in range(1, minnum+1):
            if minnum % i == 0 and maxnum % i == 0 and i > ans:
                ans = i
        return ans
