# 1844. Replace All Digits with Characters
# https://leetcode.com/problems/replace-all-digits-with-characters/
class Solution:
    def replaceDigits(self, s: str) -> str:
        s1 = ""
        for i in s:
            if i.isalpha():
                s1 += i
            else:
                s1 += chr(ord(s1[-1]) + int(i))

        return s1