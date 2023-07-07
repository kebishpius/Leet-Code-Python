class Solution(object):
    def truncateSentence(self, s, k):
        s1 = s.rsplit()
        s2 = ''
        for i in range(k):
            s2 = s2 + ' '+ s1[i]
        return s2.strip()
