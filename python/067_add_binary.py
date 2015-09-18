# https://leetcode.com/problems/add-binary/

# Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = a[::-1]
        a2 = b[::-1]
        n1 = len(a1)
        n2 = len(a2)
        # Reverse two numbers. add 0 if their lengths are not equal
        if n1 != n2:
            if n1 > n2:
                for i in range(n2, n1):
                    a2 = a2+"0"
            else:
                for i in range(n1, n2):
                    a1 = a1+"0"
        rst = ""
        carrier = 0
        # calculate the result by digits.
        for i in range(0, len(a1)):
            tmp1 = int(a1[i])
            tmp2 = int(a2[i])
            answer = tmp1 + tmp2 + carrier
            if answer == 3:
                rst = rst + "1"
                carrier = 1
            elif answer == 2:
                rst = rst + "0"
                carrier = 1
            else:
                rst = rst + str(answer)
                carrier = 0
        # check if we need to add an extra digit for the carrier.
        if carrier == 1:
            rst = rst + "1"
        # reverse the string back and return
        rst = rst[::-1]
        return rst