# https://leetcode.com/problems/reverse-bits/

# Reverse bits of a given 32 bits unsigned integer.
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
# Follow up:
# If this function is called many times, how would you optimize it?

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = ""
        while n > 0:
          rst = rst + str(n%2)
          n = n / 2
        print rst
        while len(rst)<32:
          rst = rst + "0"
        print rst
        
        # https://wiki.python.org/moin/BitManipulation

        # >>> print int('00100001', 2)
        # 33

        return int(rst, 2)
        
x = Solution()
print x.reverseBits(1)