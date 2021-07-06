# 566. Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l = [[0 for j in range(c)] for j in range(r)]
        if r * c != len(mat[0]) * len(mat):
            return mat
        q, w = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                l[q][w] = mat[i][j]
                w += 1
                if w == c:
                    q += 1
                    w = 0

        return l
