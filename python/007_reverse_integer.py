# https://leetcode.com/problems/reverse-integer/

# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution:
    # @return an integer
    def reverse(self, x):
        Negativeflag = False
        if (x < 0):
            Negativeflag = True
            x = 0 - x
        result = 0
        while (x > 0):
            mod = x % 10
            x = x / 10
            result = result * 10 + mod
        if (Negativeflag == True):
            result = 0 - result
        return result
        
        
            