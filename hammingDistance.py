# 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #  1
        #         r=0
        #         while(x>0 or y>0):
        #             r+=(x%2)^(y%2)
        #             x=x>>1
        #             y=y>>1
        #         return r

        # 2
        return bin(x ^ y).count("1")