# Last updated: 9/10/2025, 12:55:29 AM
class Solution(object):
    def digitCount(self, num):
        for i in range(len(num)):
            if num.count(str(i)) != int(num[i]):
                return False
        return True
        """
        :type num: str
        :rtype: bool
        """
        