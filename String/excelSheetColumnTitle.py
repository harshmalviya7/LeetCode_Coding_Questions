# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        while (n):
            n -= 1
            s = chr(n % 26 + 65) + s

            n = n // 26
        return s