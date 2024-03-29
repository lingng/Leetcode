# https://leetcode.com/problems/basic-calculator-ii/

# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# You may assume that the given expression is always valid.

# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokens = self.toRPN(s)
        print tokens
        return self.evalRPN(tokens)

    operators = ['+', '-', '*', '/']

    def toRPN(self, s):
        tokens, stack = [], []
        number = ''
        for c in s:
            if c.isdigit():
                number += c
            else:
                if number:
                    tokens.append(number)
                    number = ''
                if c in self.operators:
                    while len(stack) and self.getPriority(stack[-1]) >= self.getPriority(c):
                        tokens.append(stack.pop())
                    stack.append(c)
                elif c == '(':
                    stack.append(c)
                elif c == ')':
                    while len(stack) and stack[-1] != '(':
                        tokens.append(stack.pop())
                    stack.pop()
        if number:
            tokens.append(number)
        while len(stack):
            tokens.append(stack.pop())
        return tokens

    def evalRPN(self, tokens):
        operands = []
        for token in tokens:
            if token in self.operators:
                y, x = operands.pop(), operands.pop()
                operands.append(self.getVal(x, y, token))
            else:
                operands.append(int(token))
        return operands[0]
    
    def getVal(self, x, y, operator):
        return {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / y),
        }[operator](x, y)

    def getPriority(self, operator):
        return {
            '+' : 1,
            '-' : 1,
            '*' : 2,
            '/' : 2,
        }.get(operator, 0)


x = Solution()
x.calculate('(1+3)-(4+5*6)')