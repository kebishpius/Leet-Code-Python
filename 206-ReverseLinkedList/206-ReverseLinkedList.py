# Last updated: 9/10/2025, 6:36:20 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None
        while current:
            new = current.next
            current.next = prev
            prev = current
            current = new
        return prev

        



        
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        