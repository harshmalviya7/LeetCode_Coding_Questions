# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# 1351. Count Negative Numbers in a Sorted Matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        c = 0
        i = 0
        n = len(grid)
        m = len(grid[0])
        j = 0
        while (j < m and i < n):
            print(grid[i][j])
            if grid[i][j] < 0:
                c = c + (m - j)
                i += 1
                j = 0
            else:
                j += 1
            if j == m:
                i += 1
                j = 0
        print(c)
        return c

