# Last updated: 9/10/2025, 12:55:49 AM
class Solution(object):
    def kthDistinct(self, arr, k):
        check = []
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                check.append(arr[i])
            else:
                pass
        try:
            return check[k-1]
        except:
            return ""
       
       
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """