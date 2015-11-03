# https://leetcode.com/problems/bulls-and-cows/

# You are playing the following Bulls and Cows game with your friend: You write a 4-digit secret number and ask your friend to guess it. Each time your friend guesses a number, you give a hint. The hint tells your friend how many digits are in the correct positions (called "bulls") and how many digits are in the wrong positions (called "cows"). Your friend will use those hints to find out the secret number.
# For example:
# Secret number:  "1807"
# Friend's guess: "7810"
# Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".

# Please note that both secret number and friend's guess may contain duplicate digits, for example:

# Secret number:  "1123"
# Friend's guess: "0111"
# In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
# You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dictSecret = {}
        for i in range(0, len(secret)):
            if dictSecret.has_key(secret[i]):
                dictSecret[secret[i]] = dictSecret[secret[i]]+1
            else:
                dictSecret[secret[i]] = 1
        dictGuess = {}
        for i in range(0, len(guess)):
            if dictGuess.has_key(guess[i]):
                dictGuess[guess[i]] = dictGuess[guess[i]]+1
            else:
                dictGuess[guess[i]] = 1
        total = 0
        correct = 0
        for k in dictGuess:
            if dictSecret.has_key(k):
                total += min(dictSecret[k], dictGuess[k])
        for i in range(0, len(secret)):
            if secret[i] == guess[i]:
                correct += 1
        result = str(correct)+"A"+str(total-correct)+"B"
        return result

x = Solution()
print x.getHint("1123", "0111")
print x.getHint("1807", "7810")