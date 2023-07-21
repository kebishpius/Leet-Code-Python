class Solution(object):
    def addDigits(self, num):
        if num < 10:
                return num
        num = str(num)
        while len(num) % 2 !=0:
            num = num + '0'
        while int(num) >= 10:
            total = 0
            for i in range(0, len(num), 2):
                total = int(num[i]) + int(num[i+1]) + total
            num = str(total)
        return int(num)
