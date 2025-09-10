# Last updated: 9/10/2025, 12:58:26 AM
class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if dividend < 0 and divisor < 0:
            dividend = dividend * -1
            divisor = divisor * -1
            return dividend//divisor
        if dividend < 0:
            dividend = dividend * -1
            return (dividend // divisor) * -1
        if divisor < 0:
            divisor = divisor * -1
            return (dividend // divisor) * -1


        return dividend // divisor
        
        
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """