# Last updated: 9/10/2025, 12:55:02 AM
class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        for i in range(len(words)):
            temp = list(words[i])
            temp.sort()
            x = ""
            for j in temp:
                x += j
            words[i] = x
        words.sort()
        return len(words) - len(set(words))

        """
        :type words: List[str]
        :rtype: int
        """
        