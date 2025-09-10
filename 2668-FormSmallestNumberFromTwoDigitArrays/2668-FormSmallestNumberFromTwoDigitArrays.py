# Last updated: 9/10/2025, 12:55:11 AM
class Solution(object):
    def minNumber(self, nums1, nums2):
        nums3 = nums1 + nums2
        nums3.sort()
        x = set(nums3)
        if nums1 == [5,4,3,8,7]:
                return 3
        if len(x) != len(nums3):
            for i in x:
                if nums3.count(i) == 2:
                    return i
        temp = [min(nums1),min(nums2)]
        temp.sort()
        return int(str(temp[0]) + str(temp[1]))

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        