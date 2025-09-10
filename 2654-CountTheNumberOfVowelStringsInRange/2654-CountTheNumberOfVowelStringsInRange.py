# Last updated: 9/10/2025, 12:55:13 AM
class Solution(object):
    def vowelStrings(self, words, left, right):
        count = 0
        for i in range(left,right+1):
            x = words[i]
            if x[0] in "aeiou":
                if x[-1] in "aeiou":
                    count +=1
        return count
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        