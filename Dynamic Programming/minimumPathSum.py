# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        if not grid or len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        d = [[0] * (n)] * (m)
        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    d[i][j] = grid[0][0]
                elif i == 0:
                    d[i][j] = d[0][j - 1] + grid[i][j]
                elif j == 0:
                    d[i][j] = d[i - 1][0] + grid[i][j]
                else:
                    d[i][j] = min(d[i][j - 1], d[i - 1][j]) + grid[i][j]

        return d[m - 1][n - 1]

