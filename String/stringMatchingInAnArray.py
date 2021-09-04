# 1408. String Matching in an Array
# https://leetcode.com/problems/string-matching-in-an-array/
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        l = {}

        for i in range(0, len(words)):
            for j in range(0, len(words)):

                if i != j and words[i].find(words[j]) != -1:
                    l[words[j]] = 1

        return [i for i in l.keys()]
