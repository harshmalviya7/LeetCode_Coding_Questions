
# 1337. The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
from collections import defaultdict
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = defaultdict(list)
        for i in range(len(mat)):
            d[sum(mat[i])].append(i)
        d = sorted(d.items())

        l = []
        for i, j in d:
            if (len(l) >= k):
                break
            l += j
        while len(l) > k:
            l.pop()
        return l
