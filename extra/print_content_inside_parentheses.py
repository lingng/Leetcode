# Input: (ab(cd)ef)gh(i)
# Output: ab(cd)ef, cd, i
# Output all the content within the parentheses.
# Inputs are always valid.

# On-site problem for Expedia.

class Solution(object):
    def getStr(self, str1):
      if len(str1) == 0:
        return []
      index = []
      stack = []
      for i in range(0, len(str1)):
        if str1[i] == "(":
          stack.append(i)
        if str1[i] == ")":
          left = stack.pop()
          index.append([left, i])
      rst = []
      for pair in index:
        rst.append(str1[pair[0]+1 : pair[1]])
      return rst


x = Solution()
print x.getStr("(ab(cd)ef)gh(i)")