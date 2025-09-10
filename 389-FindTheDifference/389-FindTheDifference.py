# Last updated: 9/10/2025, 12:57:56 AM
class Solution(object):
    def findTheDifference(self, s, t):
        y = []
        x = []
        bigger = []
        smaller = []
        for i in s:
            x.append(i)
        for j in t:
            y.append(j)
        if len(x) > len(y):
            bigger = x
            bigger.sort()
            smaller = y
            smaller.sort()
            smaller.append('5')
        else:
            bigger = y
            bigger.sort()
            smaller = x
            smaller.sort()
            smaller.append('5')
        print(smaller)
        print(bigger)
        for k in range(len(bigger)):
            if bigger[k] != smaller[k]:
                return bigger[k]

        
        """
        :type s: str
        :type t: str
        :rtype: str
        """