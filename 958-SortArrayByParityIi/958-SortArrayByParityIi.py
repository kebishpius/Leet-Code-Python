# Last updated: 9/10/2025, 12:57:09 AM
class Solution(object):
    def sortArrayByParityII(self, nums):
        evens = []
        odds = []
        res = []
        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        for i in range(len(nums)/2):
            res.append(evens[i])
            res.append(odds[i])
        return res
            

        
        """
        :type nums: List[int]
        :rtype: List[int]
        """