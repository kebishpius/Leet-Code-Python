class Solution(object):
    def canBeEqual(self, target, arr):
        arr.sort()
        target.sort()
        if arr == target:
            return True
        else:
            return False      
