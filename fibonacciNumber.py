# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:

        def helper(n, m):
            if n == 0 or n == 1:
                return n
            if n in m:
                return m[n]
            else:
                m[n] = helper(n - 1, m) + helper(n - 2, m)
                return m[n]

        return helper(n, {})