# Last updated: 12/14/2025, 10:29:22 AM
1class Solution(object):
2    def getConcatenation(self, nums):
3        ans = []
4        n = len(nums)
5        for i in range(n):
6            ans.append(nums[i])
7        for i in range(n):
8            ans.append(nums[i])
9        return ans
10        
11
12        """
13        :type nums: List[int]
14        :rtype: List[int]
15        """
16        