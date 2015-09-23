# https://leetcode.com/problems/implement-strstr/

# Implement strStr().
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Update (2014-11-02):
# The signature of the function had been updated to return the index instead of the pointer. If you still see your function signature returns a char * or String, please click the reload button  to reset your code definition.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        needle_len = len(needle)
        print len(haystack)-needle_len
        for i in range(0, len(haystack)-needle_len+1):
            if haystack[i:i+needle_len] == needle:
                return i
        return 0

x = Solution()
print x.strStr("mississippi","pi")