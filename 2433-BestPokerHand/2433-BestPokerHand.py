# Last updated: 9/10/2025, 12:55:27 AM
class Solution(object):
    def bestHand(self, ranks, suits):
        if len(set(suits)) == 1:
            return "Flush"
        if len(set(ranks)) <= 3:
            temp = set(ranks)
            for i in temp:
                if ranks.count(i) >= 3:
                    return "Three of a Kind"
        if len(set(ranks)) != 5:
            return "Pair"
        return "High Card"
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        