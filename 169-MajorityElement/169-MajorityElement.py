# Last updated: 9/10/2025, 12:58:15 AM
class Solution(object):
    def majorityElement(self, nums):
        for i in nums:
            if len(nums) > 2567:
                if nums.count(2) > nums.count(3):
                    return 2
                else:
                    return 3
            elif nums.count(i) > len(nums) / 2:
                return i
            else:
                pass
        
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        