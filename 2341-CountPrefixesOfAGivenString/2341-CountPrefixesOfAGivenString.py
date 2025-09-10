# Last updated: 9/10/2025, 12:55:31 AM
class Solution(object):
    def countPrefixes(self, words, s):
        x=[]
        for i in range(len(words)):
            for j in range(len(s)):
                if words[i] == s[0:j+1]:
                    x.append(words[i])
                    
        return len(x)
        
        
        
        
        
        
        
        
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        