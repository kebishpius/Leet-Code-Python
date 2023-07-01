class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max = 0
        one_counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                one_counter += 1
            if nums[i] != 1 or i == len(nums) - 1:
                if one_counter > max:
                    max = one_counter
                one_counter = 0
        return max
                    
            
        """
        :type nums: List[int]
        :rtype: int
        """
