# https://leetcode.com/problems/fraction-to-recurring-decimal/

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# For example,
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negative = False
        if numerator*denominator < 0:
            negative = True
        numerator = abs(numerator)
        denominator = abs(denominator)
        numList = []
        count = 0
        loopDict = dict()
        loopStr = None
        while True:
            numList.append(str(numerator/denominator))
            count = count + 1
            numerator = 10 * (numerator % denominator)
            if numerator == 0:
                break
            loc = loopDict.get(numerator)
            if loc:
                loopStr = "".join(numList[loc:count])
                break
            loopDict[numerator] = count
        ans = numList[0]
        if len(numList) > 1:
            ans = ans + "."
        if loopStr:
            ans = ans + "".join(numList[1:len(numList)-len(loopStr)]) + "(" + loopStr + ")"
        else:
            ans = ans + "".join(numList[1:])
        if negative:
            ans = "-"+ans
        return ans