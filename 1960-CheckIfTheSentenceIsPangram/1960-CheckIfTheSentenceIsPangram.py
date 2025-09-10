# Last updated: 9/10/2025, 12:56:00 AM
class Solution(object):
    def checkIfPangram(self, sentence):
        y= ['q', 'w', 'e' , 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f','g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ]
        for i in range(26):
            if sentence.find(y[i]) == -1:
                return False
        return True