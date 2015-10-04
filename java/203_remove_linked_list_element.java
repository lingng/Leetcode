// https://leetcode.com/problems/remove-linked-list-elements/

// Remove all elements from a linked list of integers that have value val.
// Example
// Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
// Return: 1 --> 2 --> 3 --> 4 --> 5

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode tmp = new ListNode(0);
        tmp.next = head;
        ListNode h = tmp;
        ListNode t = h.next;
        while (t != null){
            if (t.val == val){
                h.next = t.next;
                t = t.next;
            }
            else{
                h = h.next;
                t = t.next;
            }
        }
        return tmp.next;
    }
}