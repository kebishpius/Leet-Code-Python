# Last updated: 9/10/2025, 12:57:03 AM
class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        x = int(0.05 * len(arr))
        for i in range(x):
            arr.pop(0)
            arr.pop(len(arr)-1)
        return sum(arr) / (len(arr) * 1.0)
        """
        :type arr: List[int]
        :rtype: float
        """
        