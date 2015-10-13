# https://leetcode.com/problems/isomorphic-strings/

# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
# For example,
# Given "egg", "add", return true.
# Given "foo", "bar", return false.
# Given "paper", "title", return true.
# Note:
# You may assume both s and t have the same length.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if len(s) == 0 or len(s) == 1:
            return True
        dic = {}
        for i in range(0, len(s)):
            if dic.has_key(s[i]):
                tmp = dic[s[i]]
                if t[i] != tmp:
                    return False
            else:
                dic[s[i]] = t[i]
        dic = {}
        for i in range(0, len(t)):
            if dic.has_key(t[i]):
                tmp = dic[t[i]]
                if s[i] != tmp:
                    return False
            else:
                dic[t[i]] = s[i]
        return True

x = Solution()
print x.isIsomorphic("foo", "bar")