# https://leetcode.com/problems/add-two-numbers/

# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1
        h1 = l1
        h2 = l2
        rst = ListNode(0)
        tmp = rst
        carrier = 0
        while h1 is not None and h2 is not None:
            num = carrier + h1.val + h2.val
            tmp.next = ListNode(num%10)
            carrier = num / 10
            h1 = h1.next
            h2 = h2.next
            tmp = tmp.next
        if h1 is None and h2 is not None:
            while h2 is not None:
                num = carrier + h2.val
                tmp.next = ListNode(num%10)
                carrier = num/10
                h2 = h2.next
                tmp = tmp.next
        if h2 is None and h1 is not None:
            while h1 is not None:
                num = carrier + h1.val
                tmp.next = ListNode(num%10)
                carrier = num/10
                h1 = h1.next
                tmp=tmp.next
        if h1 is None and h2 is None:
            if carrier == 0:
                return rst.next
            else:
                num = ListNode(carrier)
                tmp.next = num
                return rst.next