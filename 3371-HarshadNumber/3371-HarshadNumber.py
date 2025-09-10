# Last updated: 9/10/2025, 12:54:58 AM
class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        total = 0
        for i in str(x):
            total += int(i) 
        if x % total == 0:
            return total
        return -1
        """
        :type x: int
        :rtype: int
        """
        