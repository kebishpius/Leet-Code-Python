# Last updated: 9/10/2025, 12:55:14 AM
class Solution(object):
    def getCommon(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        x = nums1.intersection(nums2)
        if len(x) == 0:
            return -1
        return min(x)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        