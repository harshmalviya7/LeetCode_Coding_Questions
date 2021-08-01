# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:

        def helper(n, m):
            if n == 0:
                return n
            if n == 1 or n == 2:
                return 1
            if n in m:
                return m[n]
            else:
                m[n] = helper(n - 1, m) + helper(n - 2, m) + helper(n - 3, m)
                return m[n]

        return helper(n, {})