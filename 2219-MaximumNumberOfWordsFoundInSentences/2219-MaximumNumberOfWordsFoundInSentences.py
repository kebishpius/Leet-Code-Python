# Last updated: 9/10/2025, 12:55:44 AM
class Solution(object):
    def mostWordsFound(self, sentences):
        most = -2
        for i in sentences:
            if i.count(" ") + 1 > most:
                most = i.count(" ") + 1
        return most
        """
        :type sentences: List[str]
        :rtype: int
        """
        