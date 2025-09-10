# Last updated: 9/10/2025, 12:54:56 AM
class Solution(object):
    def addedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        if nums1[0] > nums2[0]:
            return nums2[0] - nums1[0]
        return nums2[0] - nums1[0] 
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        