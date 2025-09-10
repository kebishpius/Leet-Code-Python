# Last updated: 9/10/2025, 12:55:37 AM
class Solution(object):
    def countPairs(self, nums, k):
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0 and i != j:
                    count += 1
        return count

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        