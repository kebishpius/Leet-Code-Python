# Last updated: 9/10/2025, 12:54:54 AM
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        good = 0
        for i in nums1:
            for j in nums2:
                if i % (j*k) == 0:
                    good += 1
        return good


        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        