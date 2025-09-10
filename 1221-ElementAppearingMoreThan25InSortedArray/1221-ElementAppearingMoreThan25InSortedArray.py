# Last updated: 9/10/2025, 12:57:02 AM
class Solution(object):
    def findSpecialInteger(self, arr):
        x=0.25 
        for i in range(len(arr)):
            if float(arr.count(arr[i])) / len(arr) > x:
                return arr[i]
            else: 
                continue
        
        
        
        
        
        
        """
        :type arr: List[int]
        :rtype: int
        """
        