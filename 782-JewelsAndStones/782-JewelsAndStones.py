# Last updated: 9/10/2025, 12:57:13 AM
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewel = []
        for i in jewels:
            jewel.append(i)
        sum = 0
        for i in range(len(jewel)):
            sum = stones.count(jewel[i]) + sum
        return sum
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """