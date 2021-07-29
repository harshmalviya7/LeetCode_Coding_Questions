# Rat in a Maze Problem - I
# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
class Solution:
    def findPath(self, m, n):
        def helper(i, j, s, m, n, visited):
            if i < 0 or j < 0 or i >= n or j >= n:
                return
            if m[i][j] == 0 or visited[i][j]:
                return
            if i == n - 1 and j == n - 1:
                l.append(s)
            visited[i][j] = 1
            helper(i - 1, j, s + "U", m, n, visited)
            helper(i + 1, j, s + "D", m, n, visited)
            helper(i, j - 1, s + "L", m, n, visited)
            helper(i, j + 1, s + "R", m, n, visited)
            visited[i][j] = 0

        l = []
        visited = [[0] * n for _ in range(n)]
        if m[0][0] == 0 or m[n - 1][n - 1] == 0:
            return l
        helper(0, 0, "", m, n, visited)
        l.sort()
        return l