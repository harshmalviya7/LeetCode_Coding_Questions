# 1329. Sort the Matrix Diagonally
# https://leetcode.com/problems/sort-the-matrix-diagonally/
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        visited = [[False] * m for _ in range(n)]

        def helper(i, j, a):
            if i >= n or j >= m:
                return
            a.append(mat[i][j])
            visited[i][j] = True
            helper(i + 1, j + 1, a)

        def helper2(i, j, a, c):
            if i >= n or j >= m:
                return
            mat[i][j] = a[c]
            helper2(i + 1, j + 1, a, c + 1)

        for i in range(n):
            for j in range(m):
                a = []
                if visited[i][j]:
                    break

                helper(i, j, a)
                print(a)
                a.sort()
                print(a)
                helper2(i, j, a, 0)
        return (mat)
