# Last updated: 12/15/2025, 11:16:27 AM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def isPalindrome(self, head):
8        current = head
9        ans = ""
10        while(current != None):
11            ans += str(current.val)
12            current = current.next
13        return ans == ans[::-1]
14
15        """
16        :type head: Optional[ListNode]
17        :rtype: bool
18        """
19        