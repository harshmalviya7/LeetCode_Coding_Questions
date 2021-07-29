# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        l = []
        left, top = 0, 0
        d = 0
        while (True):
            if left > right:
                break
            for i in range(left, right + 1):
                l.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom + 1):
                l.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                l.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left])
                l.append(matrix[i][left])
            left += 1

        return l



