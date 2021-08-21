# 1252. Cells with Odd Values in a Matrix
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
from collections import defaultdict
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for i in indices:
            d1[i[0]] += 1
            d2[i[1]] += 1
        a = 0
        for i in range(m):
            for j in range(n):
                if (d1[i] + d2[j]) % 2 != 0:
                    a += 1
        return a
