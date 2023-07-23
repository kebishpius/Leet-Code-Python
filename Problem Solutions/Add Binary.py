class Solution(object):
    def addBinary(self, a, b):
        z = bin(int(str(int(b,2)+int(a,2))))
        return z[2:]
