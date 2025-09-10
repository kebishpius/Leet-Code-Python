# Last updated: 9/10/2025, 12:55:07 AM
class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()
        if prices[0] + prices[1] > money:
            return money
        return money - (prices[0] + prices[1])
        
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        