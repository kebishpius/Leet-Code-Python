# Last updated: 9/10/2025, 12:58:12 AM
class Solution(object):
    def isHappy(self, n):
        x = str(n)
        counter = 0
        y = 0
        while counter < 200:
            counter += 1
            for i in x:
                y = y + (int(i) * int(i))
            if y == 1:
                return True 
            x = str(y)
            y = 0
        return False
        """
        :type n: int
        :rtype: bool
        """