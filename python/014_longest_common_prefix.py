# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        import sys
        shortest_idx = 0
        shortest_len = sys.maxint
        for i in range(0, len(strs)):
            if len(strs[i]) < shortest_len:
                shortest_len = len(strs[i])
                shortest_idx = i
        prefix = ""
        for i in range(0, shortest_len):
            char = strs[shortest_idx][i]
            flag = True
            for j in range(0, len(strs)):
                if strs[j][i] != char:
                    flag = False
                    break
            if flag:
                prefix = prefix+char
            else:
                break
        return prefix

x = Solution()
print x.longestCommonPrefix(["aaaaaa", "aabaab", "acaaac", "abcd", "ad"])