# Last updated: 9/10/2025, 12:58:01 AM
class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)
        res = list(set(res))
        return res
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """