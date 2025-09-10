# Last updated: 9/10/2025, 12:56:47 AM
class Solution(object):
    def canBeEqual(self, target, arr):
        arr.sort()
        target.sort()
        if arr == target:
            return True
        else:
            return False        
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """