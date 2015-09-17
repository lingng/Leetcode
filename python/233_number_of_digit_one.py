# https://leetcode.com/problems/number-of-digit-one/

# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Explanation: http://www.cnblogs.com/grandyang/p/4629032.html
        res = 0
        a = 1
        b = 1
        while n > 0 : 
            res += (n + 8) / 10 * a + (n % 10 == 1) * b
            b += n % 10 * a
            a *= 10
            n /= 10
        return res

    # https://leetcode.com/discuss/54107/0-ms-recursive-solution
    def countDigitOne_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n >= 1 and n < 10: 
            return 1
        y = 1
        x = n
        while x >= 10:
            x/=10
            y*=10
        if x == 1:
            return n-y+1+self.countDigitOne(y-1)+self.countDigitOne(n%y)
        else:
            return y + x * self.countDigitOne(y-1)+self.countDigitOne(n%y)