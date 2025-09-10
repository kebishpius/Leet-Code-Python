# Last updated: 9/10/2025, 12:55:46 AM
class Solution(object):
    def countWords(self, words1, words2):
        x=[]
        y=[]
        for i in range(len(words1)):
            if words1.count(words1[i]) == 1:
                x.append(words1[i])
        for j in range(len(words2)):
            if words2.count(words2[j]) == 1:
                x.append(words2[j])
        if len(x) == 0:
            return 0
        for k in range(len(x)):
            if x.count(x[k]) == 2:
                y.append(x[k])
        return len(y)/2
                
        
        
        
        
        
        
        
        
        
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        