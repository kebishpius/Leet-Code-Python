# Last updated: 9/10/2025, 12:57:49 AM
class Solution(object):
    def findComplement(self, num):
        y=''
        x = bin(num)[2:]
        for i in range(len(x)):
            if x[i] == '0':
                y = y + '1'
            else:
                y = y + '0'
        return int(y, 2)
        """
        :type num: int
        :rtype: int
        """