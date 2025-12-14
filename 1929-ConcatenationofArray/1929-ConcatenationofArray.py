# Last updated: 12/14/2025, 10:30:54 AM
1class Solution(object):
2    def shuffle(self, nums, n):
3        ans = []
4        for i in range(n):
5            ans.append(nums[i])
6            ans.append(nums[i+n])
7        return ans
8        """
9        :type nums: List[int]
10        :type n: int
11        :rtype: List[int]
12        """
13        