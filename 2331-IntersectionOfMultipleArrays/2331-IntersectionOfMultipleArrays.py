# Last updated: 9/10/2025, 12:55:33 AM
class Solution(object):
    def intersection(self, nums):
        ans = []
        one_d_list = []
        for i in nums:
            for j in i:
                one_d_list.append(j)
        temp = list(set(one_d_list))
        for k in temp:
            if one_d_list.count(k) == len(nums):
                ans.append(k)
        ans.sort()
        return ans
            

        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        