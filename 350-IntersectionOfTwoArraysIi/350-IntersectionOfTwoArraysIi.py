# Last updated: 9/10/2025, 12:58:00 AM
class Solution(object):
    def intersect(self, nums1, nums2):
        nums3 = set(nums1 + nums2)
        ans = []
        for i in nums3:
            if i in nums1 and i in nums2:
                if nums1.count(i) < nums2.count(i):
                    for j in range(nums1.count(i)):
                        ans.append(i)
                else:
                    for j in range(nums2.count(i)):
                        ans.append(i)
        return ans
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        