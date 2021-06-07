# 476. Number Complement
# https://leetcode.com/problems/number-complement/
class Solution:
    def findComplement(self, num: int) -> int:
        a = ""
        while (num):
            a = str(num % 2 ^ 1) + a

            num >>= 1
        return int(a, 2)
