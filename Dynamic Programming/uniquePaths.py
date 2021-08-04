# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        d = [[None] * (n)] * (m)

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    d[i][j] = 1
                    continue
                d[i][j] = d[i - 1][j] + d[i][j - 1]

        return d[-1][-1]
