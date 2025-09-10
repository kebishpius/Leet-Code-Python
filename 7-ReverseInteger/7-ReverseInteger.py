# Last updated: 9/10/2025, 12:58:29 AM
class Solution(object):
    def reverse(self, x):
        x = str(x)
        y = 1
        if x[0] == '-':
            y = -1
            x = x[::-1]
            x = int(x[0:len(x)-1]) * y
            if int(x) > 2**31 - 1 or int(x) < -2**31:
                return 0
            return x
        x = x[::-1]
        if int(x) > 2**31 - 1 or int(x) < -2**31:
                return 0
        return int(x)
        
        """
        :type x: int
        :rtype: int
        """