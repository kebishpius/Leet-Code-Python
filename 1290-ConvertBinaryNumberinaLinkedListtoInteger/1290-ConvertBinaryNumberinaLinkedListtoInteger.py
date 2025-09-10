# Last updated: 9/10/2025, 6:43:34 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        current = head
        temp = ""
        while current:
            temp += str(current.val)
            current = current.next
        return int(temp,2)

        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        