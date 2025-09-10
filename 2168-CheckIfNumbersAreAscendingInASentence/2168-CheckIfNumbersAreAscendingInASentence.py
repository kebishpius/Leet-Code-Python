# Last updated: 9/10/2025, 12:55:48 AM
class Solution(object):
    def areNumbersAscending(self, s):
        x = s.split()
        temp = []
        for i in x:
            if i.isdigit():
                temp.append(int(i))
        for j in range(len(temp)-1):
            if temp[j] >= temp[j+1]:
                return False
        return True
        """
        :type s: str
        :rtype: bool
        """
        