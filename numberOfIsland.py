# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def call(grid ,i ,j):
            if i< 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return 0
            grid[i][j] = "0"

            call(grid, i + 1, j)
            call(grid, i - 1, j)
            call(grid, i, j - 1)
            call(grid, i, j + 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    call(grid, i, j)
        return count