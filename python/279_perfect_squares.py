# https://leetcode.com/problems/perfect-squares/

# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

class Solution(object):
    _dp = [0]

    # Ref: https://leetcode.com/discuss/56993/static-dp-c-12-ms-python-172-ms-ruby-384-ms
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

    # A time limit exceed approach. But easier to understand.
    def numSquares_TLE(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Or we can allocate an array with MAX_INT.
        dp = collections.defaultdict(int)
        y = 1
        while y * y <= n:
            # if the number is a square of y, then we can return 1. Eg, dp[1] = 1, dp[4] = 1, dp[9] = 1
            dp[y * y] = 1
            y += 1
        for x in range(1, n + 1):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    # x + y^2 = dp[x] + 1. This 1 is for the y^2.
                    dp[x + y * y] = dp[x] + 1
                y += 1
        return dp[n]
        
# Greedy won't work.
# Eg, n = 12. Correct answer: 3. Greedy: 9 + 2 + 1 + 1 -> 4.

# An answer using number thoery: https://leetcode.com/discuss/56982/o-sqrt-n-in-ruby-and-c