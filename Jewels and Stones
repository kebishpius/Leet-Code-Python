class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewel = []
        for i in jewels:
            jewel.append(i)
        sum = 0
        for i in range(len(jewel)):
            sum = stones.count(jewel[i]) + sum
        return sum
