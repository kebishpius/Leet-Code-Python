# Last updated: 9/10/2025, 12:55:30 AM
class Solution(object):
    def largestGoodInteger(self, num):
        x = []
        for j in num:
            x.append(j)
        ans = ""
        greatest = -1
        for i in range(len(x)-2):
            if x[i] == x[i+1] == x[i+2] and int(x[i]) > greatest:
                ans = x[i] + x[i+1] + x[i+2]
                greatest = int(x[i])
        return ans

        """
        :type num: str
        :rtype: str
        """
        