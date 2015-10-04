# https://leetcode.com/problems/remove-linked-list-elements/

# Remove all elements from a linked list of integers that have value val.
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        tmp = ListNode(0)
        tmp.next = head
        h = tmp
        t = h.next
        while t is not None:
            if t.val == val:
                h.next = t.next
                t = t.next
            else:
                h = h.next
                t = t.next
        return tmp.next