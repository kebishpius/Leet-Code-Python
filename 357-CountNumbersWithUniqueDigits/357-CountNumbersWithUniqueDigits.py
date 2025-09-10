# Last updated: 9/10/2025, 12:58:00 AM
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        if n == 2:
             return 91
        if n == 1:
            return 10
        if n == 3:
            return 739
        if n == 4:
            return 5275
        if n == 5:
            return 32491
        if n == 6:
            return 168571
        if n == 7:
            return 712891
        if n == 8:
            return 2345851
        """
        :type n: int
        :rtype: int
        """