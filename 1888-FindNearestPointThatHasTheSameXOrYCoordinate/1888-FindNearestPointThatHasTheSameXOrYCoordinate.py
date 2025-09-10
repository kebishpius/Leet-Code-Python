# Last updated: 9/10/2025, 12:59:04 AM
class Solution(object):
    def nearestValidPoint(self, x, y, points):
        ans = []
        temp = []
        for i in range(len(points)):
                if points[i][0] == x or points[i][1] == y:
                    ans.append(abs(x-points[i][0])+abs(y-points[i][1]))
                    temp.append(points[i])
        if len(ans) == 0:
            return -1
        return points.index(temp[ans.index(min(ans))])

        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        