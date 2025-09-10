# Last updated: 9/10/2025, 12:55:36 AM
class Solution(object):
    def sortEvenOdd(self, nums):
        evens = []
        odds = []
        ans = []
        for i in range(len(nums)):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        evens.sort()
        odds.sort(reverse = True)
        if len(evens) >= len(odds):
            for j in range(len(evens)):
                ans.append(evens[j])
                try:
                    ans.append(odds[j])
                except:
                    pass
        else:
            for j in range(len(odds)):
                ans.append(odds[j])
                try:
                    ans.append(evens[j])
                except:
                    pass
        return ans

            


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        