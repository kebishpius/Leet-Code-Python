# Last updated: 9/10/2025, 12:58:11 AM
class Solution(object):
    def containsDuplicate(self, nums):
        x = list(dict.fromkeys(nums))
        if len(x) == len(nums):
            return False
        else:
            return True