# Last updated: 9/10/2025, 12:55:32 AM
class Solution(object):
    def removeDigit(self, number, digit):
        temp = []
        for i in range(number.count(digit)):
            for j in range(len(number)):
                x = ""
                if number[j] == digit:
                    x = number[0:j] + number[j+1:]
                    temp.append(int(x))
        return str(max(temp))


        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        