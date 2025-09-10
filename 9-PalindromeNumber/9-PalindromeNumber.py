# Last updated: 9/10/2025, 12:58:28 AM
class Solution(object):
    def isPalindrome(self, x):
        z = str(x)
        y = z[::-1]
        if y == z:
            return True
        else:
            return False