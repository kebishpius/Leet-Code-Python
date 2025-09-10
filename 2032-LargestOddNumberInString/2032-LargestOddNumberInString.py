# Last updated: 9/10/2025, 12:55:59 AM
class Solution(object):
    def largestOddNumber(self, num):
        if int(num[len(num)-1]) % 2 == 1:
            return num
        for i in range(len(num)):
            if int(num[len(num)-1-i]) % 2 == 1:
                return num[0:len(num)-1-i+1]
        return ""
        """
        :type num: str
        :rtype: str
        """
        