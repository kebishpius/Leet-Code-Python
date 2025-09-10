# Last updated: 9/10/2025, 12:55:40 AM
class Solution(object):
    def minimumSum(self, num):
        int1 = ""
        int2 = ""
        num = list(str(num))
        for i in range(len(num)):
            num[i] = int(num[i])
        num.sort()
        int1 += str(num[0]) + str(num[2])
        int2 += str(num[1]) + str(num[3])
        return int(int1) + int(int2)
        
        """
        :type num: int
        :rtype: int
        """
        