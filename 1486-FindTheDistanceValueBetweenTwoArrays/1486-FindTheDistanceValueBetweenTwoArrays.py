# Last updated: 9/10/2025, 12:56:51 AM
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        orig_value = 1
        count = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j]) <= d and count != orig_value:
                    count += 1
            orig_value += 1
            if orig_value - count == 2:
                orig_value = orig_value - 1
        return len(arr1) - count
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        