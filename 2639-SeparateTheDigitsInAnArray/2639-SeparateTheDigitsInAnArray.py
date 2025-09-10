# Last updated: 9/10/2025, 12:55:12 AM
class Solution(object):
    def separateDigits(self, nums):
        temp = ""
        for i in nums:
            temp += str(i)
        ans = []
        for j in temp:
            ans.append(int(j))
        return ans

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        