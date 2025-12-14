# Last updated: 12/14/2025, 3:11:34 PM
1class Solution(object):
2    def findMaxConsecutiveOnes(self, nums):
3        maxCount = 0
4        count = 0
5        for i in nums:
6            if i != 0:
7                count += 1
8            else:
9                if maxCount < count:
10                    maxCount = count
11                count = 0
12        if maxCount < count:
13            maxCount = count
14        return maxCount
15                
16
17        """
18        :type nums: List[int]
19        :rtype: int
20        """
21        