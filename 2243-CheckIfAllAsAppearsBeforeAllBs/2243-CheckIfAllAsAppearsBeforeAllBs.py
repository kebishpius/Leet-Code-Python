# Last updated: 9/10/2025, 12:55:41 AM
class Solution(object):
    def checkString(self, s):
        if s.rfind('ba') == -1:
            return True
        else: 
            return False
        
        
        
        """
        :type s: str
        :rtype: bool
        """