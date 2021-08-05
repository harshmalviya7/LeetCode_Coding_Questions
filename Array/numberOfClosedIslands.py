# 1254. Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands/
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def helper(i, j, grid):
            if grid[i][j] == 1:
                return True
            if i <= 0 or i >= (len(grid) - 1) or j <= 0 or j >= (len(grid[0]) - 1):
                return False
            grid[i][j] = 1
            down = helper(i + 1, j, grid)
            right = helper(i, j + 1, grid)
            up = helper(i - 1, j, grid)
            left = helper(i, j - 1, grid)
            return up and left and right and down

        c = 0

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):

                if grid[i][j] == 0 and helper(i, j, grid):
                    c += 1

        return c