# Last updated: 1/3/2026, 2:55:10 PM
1class Solution(object):
2    def maxSubArray(self, nums):
3        if len(nums) == 1:
4             return nums[0]
5        current_sum = nums[0]
6        max_sum = nums[0]
7        
8        for i in range(1,len(nums)):
9            current = nums[i]
10            if (current_sum >= 0 and current >= 0) or (current_sum >= 0 and current < 0):
11                current_sum += current
12            else:
13                current_sum = current
14            if current_sum > max_sum:
15                max_sum = current_sum
16        return max_sum
17            
18        """
19        :type nums: List[int]
20        :rtype: int
21        """
22        