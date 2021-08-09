# 1805. Number of Different Integers in a String
# https://leetcode.com/problems/number-of-different-integers-in-a-string/
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        i = 0
        c = 0
        s = set()
        while (i < len(word)):
            if word[i].isdigit():

                a = ""
                while (i < len(word) and word[i].isdigit()):
                    a += word[i]
                    i += 1
                s.add(int(a))
            i += 1
        return len(s)


