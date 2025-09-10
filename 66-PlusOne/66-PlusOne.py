# Last updated: 9/10/2025, 12:58:22 AM
class Solution(object):
    def plusOne(self, digits):
        temp = ""
        for i in digits:
            temp += str(i)
        temp = int(temp) + 1
        temp = str(temp)
        ans = []
        for j in temp:
            ans.append(int(j))
        return ans
        