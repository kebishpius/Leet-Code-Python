# Last updated: 9/10/2025, 12:55:25 AM
class Solution(object):
    def minimumOperations(self, nums):
        temp = []
        for i in nums:
            if i != 0:
                temp.append(i)
        return len(set(temp))
        """
        :type nums: List[int]
        :rtype: int
        """
        