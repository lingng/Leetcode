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