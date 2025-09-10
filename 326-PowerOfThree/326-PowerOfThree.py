# Last updated: 9/10/2025, 12:58:04 AM
class Solution(object):
    def isPowerOfThree(self, n):
        for i in range(40):
            if 3 ** i == n:
                return True
            elif 3**i !=n:    
                for g in range(40):
                    if 3 ** g == n:
                        return True
                    else:
                        continue
            else:
                return False
        