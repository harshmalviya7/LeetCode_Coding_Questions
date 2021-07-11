# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/
class Solution:
    def balancedStringSplit(self, s: str) -> int:

        R = 0
        c = 0
        for i in s:
            if i == "R":
                R += 1
            if i == "L":
                R -= 1
            if R == 0:
                c += 1
        return c
