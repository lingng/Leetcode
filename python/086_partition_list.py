# https://leetcode.com/problems/partition-list/

# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h = head
        less = ListNode(0)
        great = ListNode(0)
        l = less
        g = great
        while h:
            if h.val < x:
                l.next = h
                h = h.next
                l = l.next
                l.next = None
            else:
                g.next = h
                h = h.next
                g = g.next
                g.next = None
        l.next = great.next
        head = less.next
        return head