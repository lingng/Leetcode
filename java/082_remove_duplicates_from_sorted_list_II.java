// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

// Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

// For example,
// Given 1->2->3->3->4->4->5, return 1->2->5.
// Given 1->1->1->2->3, return 2->3.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null){
            return null;
        }
        if (head != null && head.next == null){
            return head;
        }
        HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();
        ListNode tmp = head;
        while (tmp != null){
            if (dict.containsKey(tmp.val)){
                int val = dict.get(tmp.val);
                dict.put(tmp.val, val + 1);
            }
            else{
                dict.put(tmp.val, 1);
            }
            tmp = tmp.next;
        }

        tmp = head;
        ListNode fakehead = new ListNode(0);
        ListNode pointer = fakehead;
        while (tmp != null){
            int val = dict.get(tmp.val);
            if (val != 1){
                tmp = tmp.next;
            }
            else{
                pointer.next = new ListNode(tmp.val);
                tmp = tmp.next;
                pointer = pointer.next;
            }
        }
        return fakehead.next;
    }
}