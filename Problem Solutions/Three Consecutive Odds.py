class Solution(object):
    def threeConsecutiveOdds(self, arr):
        odd = 0
        for num in arr:
            if num % 2 == 1:
                odd += 1
                if odd >= 3:
                    return True
            else:
                odd = 0
        return False
