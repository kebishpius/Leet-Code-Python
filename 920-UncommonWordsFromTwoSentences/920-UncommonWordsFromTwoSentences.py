# Last updated: 9/10/2025, 12:57:11 AM
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s3 = s1 + " " + s2
        s4 = s3.rsplit(" ")
        answer = []
        for i in range(len(s4)):
            if s4.count(s4[i]) == 1:
                answer.append(s4[i])
        return answer

        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """