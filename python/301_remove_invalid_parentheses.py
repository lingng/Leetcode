# https://leetcode.com/problems/remove-invalid-parentheses/

# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
# Note: The input string may contain letters other than the parentheses ( and ).
# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s):
            mi = calc(s)
            if mi == 0:
                return [s]
            ans = []
            for x in range(len(s)):
                if s[x] in ('(', ')'):
                    ns = s[:x] + s[x+1:]
                    if ns not in visited and calc(ns) < mi:
                        visited.add(ns)
                        ans.extend(dfs(ns))
            return ans

        def calc(s):
            a = b = 0
            for c in s:
                a += {'(' : 1, ')' : -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        visited = set([s])
        print visited
        return dfs(s)

    def removeInvalidParentheses1(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        stack = self.checkValid(s)
        if len(stack) == 0:
            return [s]
        result = []
        visited = set([s])   
        p = 0
        self.dfs(s, stack, p, result, visited)
        return result


    def dfs(self, s, stack, p, result, visited):
        for i in range(0, len(s)):
            if p >= len(stack):
                return
            if s[i] == stack[p]:
                substr = s[:i]+s[i+1:]
                if substr not in visited:
                    visited.add(substr)
                    tmp = self.checkValid(substr)
                    if len(tmp) == 0:
                        if substr not in result:
                            result.append(substr)
                    elif len(tmp) > len(stack):
                        continue
                    else:
                        self.dfs(substr, stack, p+1, result, visited)

        
    def checkValid(self, s):
        stack = []
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append('(')
            if s[i] == ')':
                if len(stack) == 0:
                    stack.append(')')
                elif stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
        return stack

x = Solution()
print x.removeInvalidParentheses("(((k()((")
