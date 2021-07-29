# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)

        for i in range(len(matrix)):
            s = 0
            e = len(matrix[0]) - 1
            while (s < e):
                matrix[i][s], matrix[i][e] = matrix[i][e], matrix[i][s]
                s += 1
                e -= 1
        print(matrix)
        return matrix