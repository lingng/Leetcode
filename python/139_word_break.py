# https://leetcode.com/problems/word-break/

# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# Return true because "leetcode" can be segmented as "leet code".

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(0, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]

x = Solution()
print x.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])

# Use DFS will cause Time Limit Exceed. Especially in the test case above.