# Last updated: 9/10/2025, 12:55:17 AM
class Solution(object):
    def countDigits(self, num):
        count = 0
        val = list(str(num))
        print(val)
        for i in range(len(val)):
            if num % int(val[i]) == 0:
                count = count + 1
        return count
        
        """
        :type num: int
        :rtype: int
        """