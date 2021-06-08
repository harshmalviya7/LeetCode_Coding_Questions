# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:

        #         d={}
        #         d[0]=1
        #         d[1]=1

        #         for i in range(2,n+1):
        #             d[i]=d[i-1]+d[i-2]

        #         return d[n]

        def climb(i, n, m):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in m:
                return m[i]

            else:
                m[i] = climb(i + 1, n, m) + climb(i + 2, n, m)
            return m[i]

        return climb(0, n, {})

