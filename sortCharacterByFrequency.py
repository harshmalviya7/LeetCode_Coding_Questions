# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:

        chars = list(set(s))
        d = {}

        for c in chars:
            d[c] = s.count(c) s=""

        d=sorted( d .items(), key=lambda item: item[1],reverse= True)
        for k,v in d:
            s+=str(v* k)
        return s

#         d=defaultdict(int)

#         for i in range(len(s)):

#             d[s[i]]+=1

#         s=""

#         d=sorted(d.items(), key=lambda item: item[1],reverse=True)
#         for k,v in d:
#             s+=str(v*k)
#         return s
