# Last updated: 9/10/2025, 12:56:49 AM
class Solution(object):
    def findLucky(self, arr):
        x=[]
        for i in range(len(arr)):
            if arr.count(arr[i]) == arr[i]:
                x.append(arr[i])
        
        if len(x) == 0:
            return -1
        
        return max(x) 
        
        
        
        
        
        
        
        
        """
        :type arr: List[int]
        :rtype: int
        """
        