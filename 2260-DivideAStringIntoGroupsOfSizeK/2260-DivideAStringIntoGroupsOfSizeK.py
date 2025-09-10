# Last updated: 9/10/2025, 12:55:39 AM
class Solution(object):
    def divideString(self, s, k, fill):
        temp = []
        count = 0
        x = ""
        for i in range(len(s)):
            x += s[i]
            count += 1
            if count == k:
                temp.append(x)
                x = ""
                count = 0
        if x != "":
            temp.append(x)
        if len(temp[-1]) != k:
            for j in range(k-len(temp[-1])):
                temp[-1] += fill
        return temp

        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        