# Last updated: 9/10/2025, 12:56:52 AM
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        small = 0
        for i in nums:
            for j in nums:
                if i > j:
                    small += 1
            ans.append(small)
            small = 0
        return ans

        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        