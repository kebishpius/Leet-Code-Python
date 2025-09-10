# Last updated: 9/10/2025, 12:57:13 AM
class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = ["a","e","i","o","u"]
        s = sentence.split()
        temp = ""
        ans = ""
        for i in range(len(s)):
            if s[i][0].lower() in vowels:
                temp += 'ma'
            else:
                temp += s[i][0] + "ma"
                s[i] = s[i][1:]
            for j in range(i+1):
                temp += 'a'
            ans += s[i] + temp
            if i != len(s) - 1:
                ans+= " "
            temp = ""
        return ans
        


                    
            
        """
        :type sentence: str
        :rtype: str
        """
        