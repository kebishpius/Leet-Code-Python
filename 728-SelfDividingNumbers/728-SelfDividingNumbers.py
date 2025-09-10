# Last updated: 9/10/2025, 12:57:15 AM
class Solution(object):
    def selfDividingNumbers(self, left, right):
        num = ""
        ans = []
        for i in range(left,right+1):
            count = 0
            num = str(i)
            for j in num:
                if j.count("0") == 0:
                    if i % int(j) == 0:
                        count += 1
            if count == len(num):
                ans.append(i)
        return ans




        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        