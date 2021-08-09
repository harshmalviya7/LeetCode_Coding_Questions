# 415. Add Strings
# https://leetcode.com/problems/add-strings/
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        s = ""
        c = 0
        while (i >= 0 and j >= 0):
            d = ord(num1[i]) + ord(num2[j]) - 96 + c

            s = str(chr(d % 10 + 48)) + s
            c = d // 10
            i -= 1
            j -= 1
        while (i >= 0):
            d = ord(num1[i]) - 48 + c
            s = str(chr(d % 10 + 48)) + s
            c = d // 10
            i -= 1
        while (j >= 0):
            d = ord(num2[j]) - 48 + c
            s = str(chr(d % 10 + 48)) + s
            c = d // 10
            j -= 1
        if c:
            s = str(c) + s
        return s
