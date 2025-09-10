# Last updated: 9/10/2025, 12:56:39 AM
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        ans = 0
        count = 0
        for i in words:
            for j in allowed:
                count += i.count(j)
            if count == len(i):
                    ans +=1
            count = 0
        return ans
                
                
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        