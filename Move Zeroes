class Solution(object):
    def moveZeroes(self, nums):
        store = []
        counter = nums.count(0)
        for i in range(len(nums)):
            if nums[i] == 0:
                store.append(i)  
        for k in range(counter):
            nums.append(0)
        for j in range(len(store)):
            nums.remove(0)
