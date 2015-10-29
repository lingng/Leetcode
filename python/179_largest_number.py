# https://leetcode.com/problems/largest-number/

# Given a list of non negative integers, arrange them such that they form the largest number.
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num = sorted([str(x) for x in nums], cmp = self.compare)
        ans = ''.join(num).lstrip('0')
        return ans or '0'

    def compare(self, a, b):
        return [1, -1][a + b > b + a]