class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = ''
        while len(word1) < len(word2):
            word1 += '2'
        while len(word2) < len(word1):
            word2 += '2'
        for i in range(len(word1)):
            if word1[i].isalpha() == True:
                ans += word1[i]
            if word2[i].isalpha() == True:
                ans += word2[i]
        return ans
