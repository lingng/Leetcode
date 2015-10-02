# https://leetcode.com/problems/factorial-trailing-zeroes/

# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 5
        ans = 0
        while n >= a:
            ans = ans + n / a
            a = a * 5
        return ans

x = Solution()
print x.trailingZeroes(5)