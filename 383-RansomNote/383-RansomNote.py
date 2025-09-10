# Last updated: 9/10/2025, 12:57:58 AM
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for i in ransomNote:
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        