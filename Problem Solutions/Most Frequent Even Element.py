class Solution(object):
    def mostFrequentEven(self, nums):
        nodupes = list(dict.fromkeys(nums))
        onlyevens = []
        for i in range(len(nodupes)):
            if nodupes[i] % 2 == 0:
                onlyevens.append(nodupes[i])
        if len(onlyevens) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        onlyevens.sort()
        max = -99
        tracker = 0
        print(onlyevens)
        for j in(range(0, len(onlyevens))):
            if nums.count(onlyevens[j]) > max:
                max = nums.count(onlyevens[j])
                tracker = onlyevens[j]
        return tracker
