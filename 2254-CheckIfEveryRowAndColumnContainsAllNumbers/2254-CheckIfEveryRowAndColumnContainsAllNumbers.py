# Last updated: 9/10/2025, 12:55:41 AM
class Solution(object):
    def checkValid(self, matrix):
        for i in range(len(matrix[0])):
            ans = []
            count = 0
            for j in range(len(matrix[0])):
                x = matrix[j][i]
                ans.append(x)
            ans.sort()
            for k in range(len(ans)-1):
                if not (ans[k] < ans[k+1]):
                    return False
        for i in range(len(matrix[0])):
            temp = matrix[i]
            temp.sort()
            for j in range(len(temp)-1):
                if not (temp[j] < temp[j+1]):
                    return False
        return True
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        