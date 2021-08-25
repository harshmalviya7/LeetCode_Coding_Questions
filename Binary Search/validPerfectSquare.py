# 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        i = 1
        j = num
        while (i <= j):
            mid = i + (j - i) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                j = mid - 1
            else:
                i = mid + 1
        return False

