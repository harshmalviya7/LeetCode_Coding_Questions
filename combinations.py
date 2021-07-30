# 77. Combinations
# https://leetcode.com/problems/combinations/
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(res, comb, nex):
            if res == 0:
                sol.append(comb.copy())
            else:
                for i in range(nex, n + 1):
                    comb.append(i)
                    helper(res - 1, comb, i + 1)
                    comb.pop()

        sol = []
        helper(k, [], 1)
        return sol

#         l=[]
#         for i in range(1,n+1):
#             l.append(i)
#         res=combinations(l,k)
#         l=[]
#         for i in res:
#             l.append(list(i))

#         return l