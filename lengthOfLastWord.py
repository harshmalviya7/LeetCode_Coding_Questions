# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int: s=s.split( " ")
        a=0
        for i in s[::-1]:
            if i==" ":
                continue
            else:
                a=len(i)
                break
        return a



