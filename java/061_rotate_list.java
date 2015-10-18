// https://leetcode.com/problems/rotate-list/

// Given a list, rotate the list to the right by k places, where k is non-negative.

// For example:
// Given 1->2->3->4->5->NULL and k = 2,
// return 4->5->1->2->3->NULL.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null)  
        {  
            return null;  
        }  
        ListNode slow = head;  
        ListNode fast = head;  
        int idx = 0;  
        while(fast!=null && idx<k)  
        {  
            fast = fast.next;  
            idx = idx + 1;
        }  
        if(fast == null)  
        {  
            k %= idx;  
            fast = head;  
            idx=0;  
            while(fast!=null && idx<k)  
            {  
                fast = fast.next;  
                idx = idx + 1;
            }  
        }  
        while(fast.next!=null)  
        {  
            slow = slow.next;  
            fast = fast.next;  
        }  
        fast.next = head;  
        ListNode newHead = slow.next;  
        slow.next = null;  
        return newHead; 
    }
}