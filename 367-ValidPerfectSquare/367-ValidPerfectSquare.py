# Last updated: 9/10/2025, 12:57:59 AM
class Solution(object):
    def isPerfectSquare(self, num):
        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            i += 1
        return False
        """
        :type num: int
        :rtype: bool
        """
        