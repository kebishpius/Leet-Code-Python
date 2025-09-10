# Last updated: 9/10/2025, 12:57:54 AM
class Solution(object):
    def addStrings(self, num1, num2):
        return str(int(num1) + int(num2))
        x=[]
        '''if int(num1) > int(num2):
            for i in range (int(num2), int(num1) + 1):
                if i == int(num2):
                    x.append(int(num2))
                elif i == int(num1):
                    x.append(int(num1))
                else:
                    pass
        if int(num2) > int(num1):
            for i in range (int(num1), int(num2) + 1):
                if i == int(num1):
                    x.append(int(num1))
                elif i == int(num2):
                    x.append(int(num2))
                else:
                    pass
        if int(num2) == int(num1):
            
        return str(sum(x))
        '''