# Last updated: 9/10/2025, 12:57:17 AM
class Solution(object):
    def judgeCircle(self, moves):
        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
            return True
        return False
        
        """
        :type moves: str
        :rtype: bool
        """