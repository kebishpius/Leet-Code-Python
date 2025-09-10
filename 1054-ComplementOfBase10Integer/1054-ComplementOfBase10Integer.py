# Last updated: 9/10/2025, 12:57:06 AM
class Solution(object):
    def bitwiseComplement(self, n):
        x = bin(n)
        res = ''
        for i in x[2:]:
            if i == '1':
                res += '0'
            else:
                res += '1' 
        return int(res,2)


        """
        :type n: int
        :rtype: int
        """