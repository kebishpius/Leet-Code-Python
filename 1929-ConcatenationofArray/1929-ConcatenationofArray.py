# Last updated: 12/14/2025, 3:10:16 PM
1class Solution(object):
2    def findMaxConsecutiveOnes(self, nums):
3        max = 0
4        one_counter = 0
5        for i in range(len(nums)):
6            if nums[i] == 1:
7                one_counter += 1
8            if nums[i] != 1 or i == len(nums) - 1:
9                if one_counter > max:
10                    max = one_counter
11                one_counter = 0
12            print(one_counter)
13            print(max)
14            print()
15        return max
16                    
17            
18        """
19        :type nums: List[int]
20        :rtype: int
21        """