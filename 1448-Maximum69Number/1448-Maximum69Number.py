# Last updated: 9/10/2025, 12:56:55 AM
class Solution(object):
    def maximum69Number (self, num):
        num = str(num)
        num = num.replace("6","9",1)
        return int(num)