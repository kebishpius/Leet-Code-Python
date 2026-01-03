// Last updated: 1/3/2026, 1:32:30 PM
1/**
2 * Definition for singly-linked list.
3 * public class ListNode {
4 *     int val;
5 *     ListNode next;
6 *     ListNode() {}
7 *     ListNode(int val) { this.val = val; }
8 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
9 * }
10 */
11class Solution {
12    public ListNode middleNode(ListNode head) {
13        ListNode fast = head;
14        ListNode slow = head;
15        while(fast != null){
16            fast = fast.next;
17            if(fast != null){
18                fast = fast.next;
19            }
20            else{
21                break;
22            }
23            slow = slow.next;
24        }
25        return slow;
26    }
27}