# Last updated: 9/10/2025, 12:58:03 AM
class Solution(object):
    def topKFrequent(self, nums, k):
        no_dupes = list(set(nums))
        maxes = []
        kmaxes = []
        res = []
        for i in no_dupes:
            maxes.append(nums.count(i))
        for i in range(k):
            kmaxes.append(max(maxes))
            maxes.remove(max(maxes))
        for i in no_dupes:
            if nums.count(i) in kmaxes:
                res.append(i)
        return res


        

            
            
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """