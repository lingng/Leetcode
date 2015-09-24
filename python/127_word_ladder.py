# https://leetcode.com/problems/word-ladder/

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = collections.deque([(beginWord, 1)])
        ls = string.ascii_lowercase
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in xrange(len(word)):
                for j in ls:
                    if j != word[i]:
                        newWord = word[:i]+j+word[i+1:]
                        if newWord not in visited and newWord in wordList:
                            queue.append((newWord, dist+1))
                            visited.add(newWord)
        return 0

    def ladderLength_1(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        q = []
        q.append((beginWord, 0))
        while q:
            curr = q.pop(0)
            currlen = curr[1]
            currword = curr[0]
            if currword == endWord:
                return currlen+1
            for i in range(len(beginWord)):
                part1 = currword[:i]
                part2 = currword[i+1:]
                for j in "abcdefghijiklmnopqrstuvwxyz":
                    if currword[i] != j:
                        nextword = part1+j+part2
                        if nextword in wordList:
                            q.append((nextword, currlen+1))
                            wordList.remove(nextword)
        return 0