# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        n = len(matrix)
        m = len(matrix[0])
        high = (n * m) - 1

        while (low <= high):
            mid = low + (high - low) // 2
            if matrix[mid // m][mid % m] == target:
                return True
            elif matrix[mid // m][mid % m] >= target:
                high = mid - 1
            else:
                low = mid + 1

        return False