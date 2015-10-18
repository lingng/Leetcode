// https://leetcode.com/problems/merge-two-sorted-lists/

// Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null & l2 == null){
            return null;
        }
        if (l1 == null && l2 != null){
            return l2;
        }
        if (l1 != null && l2 == null){
            return l1;
        }
        ListNode tmp = new ListNode(0);
        ListNode tmp1 = tmp;
        while (l1 != null && l2 != null){
            if (l1.val <= l2.val){
                tmp1.next = new ListNode(l1.val);
                tmp1 = tmp1.next;
                l1 = l1.next;
            }
            else{
                tmp1.next = new ListNode(l2.val);
                tmp1 = tmp1.next;
                l2 = l2.next;
            }
        }
        if (l1 == null && l2 != null){
            tmp1.next = l2;
        }
        if (l1 != null && l2 == null){
            tmp1.next = l1;
        }
        return tmp.next;
    }
}