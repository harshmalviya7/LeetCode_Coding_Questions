# 867. Transpose Matrix
# https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r=len(matrix)
        c=len(matrix[0])
        l=[[None]*r for _ in range(c)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j])
                l[j][i]=matrix[i][j]
        return l