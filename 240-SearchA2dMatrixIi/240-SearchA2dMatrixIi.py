# Last updated: 9/10/2025, 12:58:08 AM
class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            target_count = i.count(target)
            if target_count != 0:
                break
        if target_count != 0:
            return True
        return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """