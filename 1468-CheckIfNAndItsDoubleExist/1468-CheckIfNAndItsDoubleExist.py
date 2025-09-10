# Last updated: 9/10/2025, 12:56:53 AM
class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False
        """
        :type arr: List[int]
        :rtype: bool
        """
        