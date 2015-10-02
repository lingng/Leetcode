# https://leetcode.com/problems/factorial-trailing-zeroes/

# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # consider the factors of the number.
        # 2 * 5 -> one 0.
        # 10 can be divided as 2 * 5.
        # There will always be more 2 than 5. => decided by how many 5 as the factors.
        a = 5
        ans = 0
        while n >= a:
            ans = ans + n / a
            a = a * 5
        return ans

x = Solution()
print x.trailingZeroes(5)