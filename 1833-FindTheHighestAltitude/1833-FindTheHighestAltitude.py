# Last updated: 9/10/2025, 12:56:36 AM
class Solution(object):
    def largestAltitude(self, gain):
        x = [0]
        y = 0
        for i in range(len(gain)):
            y = y + gain[i]
            x.append(y)
        return max(x)

        """
        :type gain: List[int]
        :rtype: int
        """