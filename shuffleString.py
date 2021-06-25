# 1528. Shuffle String

# https://leetcode.com/problems/shuffle-string/


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str: l=[0]*len(s)

        for i,j in enume rate(indices):
            l[j]=s[i]


        return "".

        join(l)
