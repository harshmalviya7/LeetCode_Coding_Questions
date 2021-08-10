# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while (n):
            if n % 2 == 1:
                c += 1
            n = n >> 1
        return c
