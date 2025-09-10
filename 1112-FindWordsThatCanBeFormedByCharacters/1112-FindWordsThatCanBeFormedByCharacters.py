# Last updated: 9/10/2025, 12:57:05 AM
class Solution(object):
    def countCharacters(self, words, chars):
        ans = []
        final = 0
        count = 0
        chars1 = chars
        for i in range(len(words)):
            for j in range(len(words[i])):
                if chars.count(words[i][j]) >= words[i].count(words[i][j]):
                    count += 1
                    chars.replace(words[i][j], "")
            if count == len(words[i]):
                ans.append(words[i])
            count = 0
            chars = chars1
        for k in ans:
            final += len(k)
        return final
            

        