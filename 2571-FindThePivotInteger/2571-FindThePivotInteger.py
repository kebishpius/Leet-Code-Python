# Last updated: 9/10/2025, 12:55:19 AM
class Solution(object):
    def pivotInteger(self, n):
        temp = []
        for i in range(n+1):
            temp.append(i)
        print(temp)
        for i in range(1,len(temp)):
            print(sum(temp[1:i+1]))
            print(sum(temp[i:]))
            print('')
            if sum(temp[1:i+1]) == sum(temp[i:]):
                return i
        return -1
        """
        :type n: int
        :rtype: int
        """
        