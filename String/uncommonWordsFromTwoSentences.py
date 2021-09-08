# 884. Uncommon Words from Two Sentences
# https://leetcode.com/problems/uncommon-words-from-two-sentences/
"""Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana""""
# Output: ["banana"]

from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        d = defaultdict(int)
        for i in s1.split() + s2.split():
            d[i] += 1

        l = []
        for i in d:
            if d[i] == 1:
                l.append(i)
        return l
