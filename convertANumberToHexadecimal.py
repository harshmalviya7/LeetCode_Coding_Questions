# 405. Convert a Number to Hexadecimal

# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
class Solution:
    def toHex(self, num: int) -> str:
        d = "0123456789abcdef"
        c = ""
        if num < 0:
            num = 2 ** 32 + num
        if num == 0:
            return "0"
        while (num):
            c = d[num % 16] + c
            num //= 16
        return c
