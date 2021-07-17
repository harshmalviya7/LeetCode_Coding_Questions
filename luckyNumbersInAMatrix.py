# 1380. Lucky Numbers in a Matrix
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        n = len(matrix)
        m = len(matrix[0])

        def helper(matrix, i, j, minn, a):
            for k in range(n):
                if k != i and minn < matrix[k][j]:
                    return
            a.append(minn)

        a = []
        for i in range(n):
            # minn=float("inf")
            # for j in range(m):
            #     if minn>matrix[i][j]:
            #         minn=matrix[i][j]
            #         indexj=j
            m = min(matrix[i])

            helper(matrix, i, matrix[i].index(m), m, a)
        return (a)
