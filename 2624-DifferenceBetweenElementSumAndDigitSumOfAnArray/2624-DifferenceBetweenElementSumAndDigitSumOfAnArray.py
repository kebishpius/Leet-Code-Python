# Last updated: 9/10/2025, 12:55:15 AM
class Solution(object):
    def differenceOfSum(self, nums):
        x = sum(nums)
        temp = ""
        for i in nums:
            temp += str(i)
        summ = 0
        for j in temp:
            summ += int(j)
        return abs(summ-x)


        """
        :type nums: List[int]
        :rtype: int
        """
        