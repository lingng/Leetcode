// https://leetcode.com/problems/reverse-linked-list/

// Reverse a singly linked list.
// A linked list can be reversed either iteratively or recursively. Could you implement both?
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// Iteratively.
public class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null){
            return null;
        }
        if (head != null && head.next == null){
            return head;
        }
        ListNode result = null;
        while (head != null){
            ListNode tmp = head.next;
            head.next = result;
            result = head;
            head = tmp;
        }
        return result;
    }
}