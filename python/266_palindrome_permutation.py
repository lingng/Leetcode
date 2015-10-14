# Given a string, determine if a permutation of the string could form a palindrome.

# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.

# Hint:

# Consider the palindromes of odd vs even length. What difference do you notice?
# Count the frequency of each character.
# If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?


class Solution(object):
    def palindromePermutation(self, s):
        """
        :type s: string
        :rtype: bool
        """
        dic = {}
        for i in range(0, len(s)):
            if dic.has_key(s[i]):
                dic.pop(s[i], None)
            else:
                dic[s[i]] = 1
        if len(s) % 2 == 0:
            if len(dic) == 0:
                return True
            else:
                return False
        else:
            if len(dic) == 1:
                return True
            else:
                return False

x = Solution()
print x.palindromePermutation("code")