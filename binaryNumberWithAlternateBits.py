# 693. Binary Number with Alternating Bits

# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)
        return "11" not in b and "00" not in b

#         a=n%2
#         n=n>>1

#         while(n):
#             b=n%2
#             if a==b:
#                 return False
#             n=n>>1
#             a=b
#         return True



