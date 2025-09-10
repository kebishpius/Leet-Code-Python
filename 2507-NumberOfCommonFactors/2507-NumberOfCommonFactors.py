# Last updated: 9/10/2025, 12:55:23 AM
class Solution(object):
    def commonFactors(self, a, b):
        count = 0
        if a > b:
            for i in range(1, b+1):
                if a % i == 0 and b % i == 0:
                    count = count + 1
        else:
            for i in range(1, a+1):
                if a % i == 0 and b % i == 0:
                    count = count + 1
        return count
        """
        :type a: int
        :type b: int
        :rtype: int
        """