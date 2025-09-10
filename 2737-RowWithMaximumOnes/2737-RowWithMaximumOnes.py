# Last updated: 9/10/2025, 12:55:09 AM
class Solution(object):
    def rowAndMaximumOnes(self, mat):
        x = []
        for i in mat:
            x.append(i.count(1))
        return [x.index(max(x)),max(x)]
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        