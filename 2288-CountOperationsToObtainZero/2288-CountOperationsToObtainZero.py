# Last updated: 9/10/2025, 12:55:36 AM
class Solution(object):
    def countOperations(self, num1, num2):
        counter = 0
        while True:
            if num1 == 0 or num2 == 0:
                break
            elif num1 > num2:
                num1 = num1 - num2
                counter+=1
            elif num1 < num2:
                num2 = num2-num1
                counter+=1
            elif num1 == num2:
                num1 = num1 - num2
                counter+=1
        return counter
        
        
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """