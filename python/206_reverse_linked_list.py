# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Use extra space with the same size of the linked list
        tmph = ListNode(0)
        h = head
        while h != None:
            new = ListNode(h.val)
            new.next = tmph.next
            tmph.next = new
            h = h.next
        return tmph.next


    def reverseList(self, head):
        # use constant extra space
        newhead = None
        while head != None:
            tmp = head.next
            head.next = newhead
            newhead = head
            head = tmp
        return newhead