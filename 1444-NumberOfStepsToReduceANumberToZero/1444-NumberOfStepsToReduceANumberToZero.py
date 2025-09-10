# Last updated: 9/10/2025, 12:56:55 AM
class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
                steps = steps + 1 
            else: 
                num = num - 1
                steps = steps + 1
        return steps
        
        """
        :type num: int
        :rtype: int
        """