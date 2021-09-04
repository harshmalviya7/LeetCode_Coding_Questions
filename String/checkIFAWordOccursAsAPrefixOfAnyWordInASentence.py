# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
class Solution:

    def isPrefixOfWord(self, s: str, searchWord: str) -> int:

        s = s.split()
        a = len(searchWord)
        for i in range(len(s)):
            if s[i][:a] == searchWord:
                return i + 1
        return -1

