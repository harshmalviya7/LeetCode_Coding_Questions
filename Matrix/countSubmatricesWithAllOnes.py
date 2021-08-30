# 1504. Count Submatrices With All Ones
# https://leetcode.com/problems/count-submatrices-with-all-ones/
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        for i in range(len(mat)):

            for j in range(len(mat[0]) - 2, -1, -1):

                if mat[i][j] != 0:
                    mat[i][j] = mat[i][j + 1] + 1

        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                m = mat[i][j]
                for k in range(i, len(mat)):
                    if mat[k][j] == 0:
                        break
                    m = min(m, mat[k][j])
                    count += m
        return count

