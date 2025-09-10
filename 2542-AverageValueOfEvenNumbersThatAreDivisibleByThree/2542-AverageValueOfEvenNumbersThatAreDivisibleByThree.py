# Last updated: 9/10/2025, 12:55:21 AM
class Solution(object):
    def averageValue(self, nums):
        even = []
        three = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
        for j in range(len(even)):
            if even[j] % 3 == 0:
                three.append(even[j])
        try:
            return sum(three)/len(three)
        except:
            return 0
        """
        :type nums: List[int]
        :rtype: int
        """