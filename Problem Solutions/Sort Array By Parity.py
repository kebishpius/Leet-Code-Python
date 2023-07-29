class Solution(object):
    def sortArrayByParity(self, nums):
        evens = []
        odds = []
        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        evens.extend(odds)
        return evens
