class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split(" ")):
            return False
        if len(pattern) == 0 or len(pattern) == 1:
            return True
        table = {}
        for i in range(0, len(pattern)):
            if table.has_key(pattern[i]):
                tmp = table[pattern[i]]
                if string.split(" ")[i] != tmp:
                    return False
            else:
                table[pattern[i]] = string.split(" ")[i]
        table = {}
        for i in range(0, len(pattern)):
            if table.has_key(string.split(" ")[i]):
                tmp = table[string.split(" ")[i]]
                if pattern[i] != tmp:
                    return False
            else:
                table[string.split(" ")[i]] = pattern[i]
        return True

x = Solution()
print x.wordPattern("abba", "dog dog dog dog")