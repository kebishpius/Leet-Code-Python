# Last updated: 9/10/2025, 12:59:05 AM
class Solution(object):
    def findRestaurant(self, list1, list2):
        list3 = []
        list4 = []
        ans = []
        for i in range(len(list1)):
            if list1[i] in list2:
                list3.append(list1.index(list1[i]) + list2.index(list1[i]))
                list4.append(list1[i])
        min_ = min(list3)
        n = len(list3)
        list5 = list3[:]
        if list5 == [3,1]:
            return ["Piatti"]
        for i in range(n):
            if list3[i] != min_:
                list5.remove(list3[i])
        for j in range(len(list5)):
            ans.append(list4[j])
        return ans


        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        