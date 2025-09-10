# Last updated: 9/10/2025, 12:56:59 AM
class Solution(object):
    def findDifference(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        answer = []
        temp = []
        for i in nums1:
            if i not in nums2:
                temp.append(i)
        answer.append(temp)
        temp = []
        for j in nums2:
            if j not in nums1:
                temp.append(j)
        answer.append(temp)
        return answer
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """