# Last updated: 9/10/2025, 12:58:09 AM
class Solution(object):
    def isAnagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)
        
        
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        