# Last updated: 9/10/2025, 12:58:13 AM
class Solution(object):
    def hammingWeight(self, n):
        x = str(bin(n)[2:])
        return x.count("1")

        """
        :type n: int
        :rtype: int
        """
        