# Last updated: 1/3/2026, 12:36:13 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution(object):
8    def hasCycle(self, head):
9        slow = head
10        fast = head
11        while(slow != None and fast != None):
12            slow = slow.next
13            fast = fast.next
14            if fast != None:
15                fast = fast.next
16                if(slow == fast):
17                   return True
18        return False
19
20        """
21        :type head: ListNode
22        :rtype: bool
23        """
24        