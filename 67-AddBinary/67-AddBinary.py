# Last updated: 9/10/2025, 12:58:21 AM
class Solution(object):
    def addBinary(self, a, b):
        z = bin(int(str(int(b,2)+int(a,2))))
        return z[2:]

        
        """
        :type a: str
        :type b: str
        :rtype: str
        """