# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0, 32):
            l = n & 1
            rev = l << (31 - i)
            res = res | rev
            n = n >> 1
        return res


