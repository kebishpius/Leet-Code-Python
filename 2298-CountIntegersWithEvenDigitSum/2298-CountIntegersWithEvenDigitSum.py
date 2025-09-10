# Last updated: 9/10/2025, 12:55:34 AM
class Solution(object):
    def countEven(self, num):
        total = 0
        count = 0
        for i in range(1, num+1):
            x = str(i)
            for j in str(i):
                total += int(j)
            if total % 2 == 0:
                count += 1
            total = 0
        return count
        """
        :type num: int
        :rtype: int
        """
        