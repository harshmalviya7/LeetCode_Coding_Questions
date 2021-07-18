# 1572. Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            s += mat[i][i] + mat[i][n - i - 1]
        if n % 2:
            s -= mat[n // 2][n // 2]
        return s
