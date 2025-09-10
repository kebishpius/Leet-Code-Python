# Last updated: 9/10/2025, 12:57:07 AM
class Solution(object):
    def addToArrayForm(self, num, k):
        x = ''
        for i in num:
            x += str(i)
        x = int(x) + k
        num = list(str(x))
        ans = []
        for i in num:
            ans.append(int(i))
        return ans

        
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """