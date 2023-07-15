class Solution(object):
    def majorityElement(self, nums):
        nodupes = list(dict.fromkeys(nums))
        ans = []
        for i in range(len(nodupes)):
            if nums.count(nodupes[i]) > len(nums)/3:
                ans.append(nodupes[i])
        return ans
