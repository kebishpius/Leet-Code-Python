# Last updated: 9/10/2025, 12:58:07 AM
class Solution(object):
    def addDigits(self, num):
        if num < 10:
                return num
        num = str(num)
        while len(num) % 2 !=0:
            num = num + '0'
        while int(num) >= 10:
            total = 0
            for i in num:
                total += int(i) 
            num = str(total)
        return int(num)
        

            


        """
        :type num: int
        :rtype: int
        """