# Last updated: 9/10/2025, 12:55:17 AM
class Solution(object):
    def maximumValue(self, strs):
        temp = []
        for i in strs:
            if i.isdigit():
                temp.append(int(i))
            else:
                temp.append(len(i))
        return max(temp)

        """
        :type strs: List[str]
        :rtype: int
        """
        