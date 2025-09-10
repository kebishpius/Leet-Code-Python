# Last updated: 9/10/2025, 12:58:04 AM
class Solution(object):
    def isPowerOfFour(self, n):
        for i in range(25):
            if 4 ** i == n:
                return True
            elif 4**i !=n:    
                for g in range(25):
                    if 4 ** g == n:
                        return True
                    else:
                        continue
            else:
                return False
        
        