class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            target_count = i.count(target)
            if target_count != 0:
                break
        if target_count != 0:
            return True
        return False
