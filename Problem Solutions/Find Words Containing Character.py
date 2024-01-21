class Solution(object):
    def findWordsContaining(self, words, x):
        ans = []
        for i in range(len(words)):
            if words[i].find(x) != -1:
                ans.append(i)
        return ans
