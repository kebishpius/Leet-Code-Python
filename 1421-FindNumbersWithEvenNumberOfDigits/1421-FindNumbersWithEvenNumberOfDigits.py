# Last updated: 9/10/2025, 12:56:58 AM
class Solution(object):
    def findNumbers(self, nums):
        digits = 0
        evens_count = 0
        for i in nums:
            while i != 0:
                i = i/10
                digits += 1
            print(digits)
            if digits % 2 == 0:
                evens_count+=1
            digits = 0
        return evens_count
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        