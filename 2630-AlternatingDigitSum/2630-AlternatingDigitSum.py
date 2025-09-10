# Last updated: 9/10/2025, 12:55:14 AM
class Solution(object):
    def alternateDigitSum(self, n):
        total = 0
        n = str(n)
        for i in range(len(n)):
            if i % 2 == 1:
                total -= int(n[i])
            else:
                total += int(n[i])
        return total
        """
        :type n: int
        :rtype: int
        """
        