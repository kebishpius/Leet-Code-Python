# Last updated: 9/10/2025, 12:57:12 AM
class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            image[i].reverse()
        for j in range(len(image)):
            for k in range(len(image[j])):
                if image[j][k] == 1:
                    image[j][k] = 0
                else:
                    image[j][k] = 1
        return image
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        