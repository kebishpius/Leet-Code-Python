class Solution(object):
    def maximumWealth(self, accounts):
        MAX = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            if wealth > MAX:
                MAX = wealth
        return MAX
