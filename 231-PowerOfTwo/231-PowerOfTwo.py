# Last updated: 9/10/2025, 12:58:09 AM
class Solution(object):
    def isPowerOfTwo(self, n):
        for i in range(100):
            if 2 ** i == n:
                return True
            elif 2**i !=n:    
                for g in range(100):
                    if 2 ** g == n:
                        return True
                    else:
                        continue
            else:
                return False
        