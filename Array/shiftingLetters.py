# 848. Shifting Letters
# https://leetcode.com/problems/shifting-letters/
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        count=0
        a=""
        for i in range(len(s)-1,-1,-1):
            count=(count+shifts[i])%26
            a=chr((ord(s[i])+count-ord("a"))%26 + 97)+a
        return a