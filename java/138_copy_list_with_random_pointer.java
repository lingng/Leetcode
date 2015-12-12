// https://leetcode.com/problems/copy-list-with-random-pointer/
//
// A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
// Return a deep copy of the list.

/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null){
            return null;
        }
        RandomListNode p = head;
        RandomListNode newHead = new RandomListNode(head.label);
        RandomListNode q = newHead;
        HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        map.put(p, q);
        p = p.next;
        while (p != null){
            RandomListNode tmp = new RandomListNode(p.label);
            q.next = tmp;
            map.put(p, tmp);
            p = p.next;
            q = q.next;
        }
        p = head;
        q = newHead;
        while (p!=null){
            if (p.random == null){
                q.random = null;
            }
            else{
                q.random = map.get(p.random);
            }
            p = p.next;
            q = q.next;
        }
        return newHead;
    }
}
