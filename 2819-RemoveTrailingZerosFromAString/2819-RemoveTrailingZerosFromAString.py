# Last updated: 9/10/2025, 12:55:04 AM
class Solution(object):
    def removeTrailingZeros(self, num):
        end = len(num)-1
        while True:
            if num[end] == "0":
                end -= 1
            else:
                return num[0:end+1]
        """
        :type num: str
        :rtype: str
        """
        