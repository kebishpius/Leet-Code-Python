# Last updated: 9/10/2025, 12:57:04 AM
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        

class Solution(object):
    def heightChecker(self, heights):
        counter = 0
        expected = []
        for i in range(len(heights)):
            expected.append(heights[i])
        expected.sort()
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                counter+=1
            else:
                pass
        return counter