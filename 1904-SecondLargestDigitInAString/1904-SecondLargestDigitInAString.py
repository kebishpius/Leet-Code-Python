# Last updated: 9/10/2025, 12:56:04 AM
class Solution(object):
    def secondHighest(self, s):
        temp = []
        for i in s:
            if i.isdigit():
                temp.append(int(i))
        print(temp)
        if len(temp) == 0:
            return -1
        temp = set(temp)
        temp = list(temp)
        print(temp)
        if len(temp) < 2:
            return -1
        temp.sort()
        temp.remove(max(temp))
        return max(temp)


        """
        :type s: str
        :rtype: int
        """
        