# Last updated: 9/10/2025, 12:56:58 AM
import numpy
class Solution(object):
    def subtractProductAndSum(self, n):
        y=''
        z=[]
        x=n
        y=str(x)
        for i in range(len(y)):
            z.append(int(y[i]))
        
        
        return numpy.prod(z) - sum(z)
        