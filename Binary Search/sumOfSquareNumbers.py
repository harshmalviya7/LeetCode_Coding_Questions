# 633. Sum of Square Numbers
# https://leetcode.com/problems/sum-of-square-numbers/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0: return True

        def helper(i, j, m):
            while (i <= j):
                mid = i + (j - i) // 2
                if mid * mid == m:
                    return True
                elif mid * mid > m:
                    j = mid - 1
                else:
                    i = mid + 1

            return False

        for i in range(0, c):  ##for i=0 i**2<c
            if i ** 2 > c:
                break
            m = c - i * i

            if helper(0, m, m):
                return True
        return False