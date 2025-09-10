# Last updated: 9/10/2025, 12:57:00 AM
class Solution(object):
    def uniqueOccurrences(self, arr):
        arr.sort()
        x = set(arr)
        x = list(x)
        temp = []
        for i in x:
            temp.append(arr.count(i))
        temp = set(temp)
        temp = list(temp)
        return len(temp) == len(x)
        """
        :type arr: List[int]
        :rtype: bool
        """
        