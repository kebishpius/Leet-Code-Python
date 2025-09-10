# Last updated: 9/10/2025, 12:56:38 AM
class Solution(object):
    def halvesAreAlike(self, s):
        countx = 0
        county = 0
        x = s[0:len(s)/2]
        y = s[len(s)/2: len(s)]
        for i in range(len(s)/2):
            if y[i] == 'a' or y[i] == 'e' or y[i] == 'i' or y[i] == 'o' or y[i] == 'u' or y[i] == 'A' or y[i] == 'E' or y[i] == 'I' or y[i] == 'O' or y[i] == 'U':
                county = county + 1
            if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u' or x[i] == 'A' or x[i] == 'E' or x[i] == 'I' or x[i] == 'O' or x[i] == 'U': 
                countx= countx+1
        if countx == county:
            return True
        return False

        """
        :type s: str
        :rtype: bool
        """