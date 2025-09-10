# Last updated: 9/10/2025, 12:58:10 AM
class Solution(object):
    def majorityElement(self, nums):
        nodupes = list(dict.fromkeys(nums))
        ans = []
        for i in range(len(nodupes)):
            if nums.count(nodupes[i]) > len(nums)/3:
                ans.append(nodupes[i])
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """