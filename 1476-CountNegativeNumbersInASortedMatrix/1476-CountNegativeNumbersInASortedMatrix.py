# Last updated: 9/10/2025, 12:56:53 AM
class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count += 1
        return count
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        