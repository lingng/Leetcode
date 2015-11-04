# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxlen = 0
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = -1
        for i in range(len(s)):
            if dic[s[i]] != -1:
                while start <= dic[s[i]]:
                    dic[s[start]] = -1
                    start += 1
            if i - start + 1 > maxlen: maxlen = i - start + 1
            dic[s[i]] = i
        return maxlen


x = Solution()
print x.lengthOfLongestSubstring('aababcabcda')