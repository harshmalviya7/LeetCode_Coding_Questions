# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/

import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str: d=collecti ons.defaultdict(int)
        for i in t:
            d[i]+=1
        for i in s:
            d[i]-=1


        for i,j

        in d.items():
            if j>0:
                return i


