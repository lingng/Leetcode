// https://leetcode.com/problems/reverse-linked-list-ii/

// Reverse a linked list from position m to n. Do it in-place and in one-pass.

// For example:
// Given 1->2->3->4->5->NULL, m = 2 and n = 4,

// return 1->4->3->2->5->NULL.

// Note:
// Given m, n satisfy the following condition:
// 1 ≤ m ≤ n ≤ length of list.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if ((head == null) || (head != null && head.next == null)){
            return head;
        }
        if (m == n){
            return head;
        }
        ListNode fakehead = new ListNode(0);
        fakehead.next = head;
        ListNode prem = fakehead;
        ListNode postn = fakehead;
        int m1 = 0;
        int n1 = 0;
        while (m1 < m - 1){
            prem = prem.next;
            m1 = m1 + 1;
        }
        while (n1 < n + 1){
            postn = postn.next;
            n1 = n1 + 1;
        }
        ListNode tmpTail = postn;
        ListNode tmphead = prem.next;
        while (tmphead != postn){
            ListNode tmpNext = tmphead.next;
            tmphead.next = tmpTail;
            tmpTail = tmphead;
            tmphead = tmpNext;
        }
        prem.next = tmpTail;
        return fakehead.next;
    }
}