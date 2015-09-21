# https://leetcode.com/problems/palindrome-linked-list/

# Given a singly linked list, determine if it is a palindrome.
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        h1 = head
        count = 0
        while h1 is not None:
            count = count + 1
            h1 = h1.next
        length = count
        if length == 0 or length == 1:
            return True
        ind = 0
        if length % 2 == 0:
            ind = length / 2
            print ind
            count = 0
            h1 = head
            stack = []
            while count < ind:
                count = count + 1
                stack.append(h1.val) 
                h1 = h1.next
            while h1 is not None:
              val = stack.pop()
              if h1.val != val:
                return False
              h1 = h1.next
            return True
        else:
            ind = length / 2
            print ind
            count = 0
            h1 = head
            stack = []
            while count < ind:
                count = count + 1
                stack.append(h1.val)
                h1 = h1.next
            h1 = h1.next
            while h1 is not None:
                val = stack.pop()
                if h1.val != val:
                    return False
                h1 = h1.next
            return True