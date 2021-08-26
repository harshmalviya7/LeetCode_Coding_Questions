# 1304. Find N Unique Integers Sum up to Zero
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = []
        if n % 2 != 0:
            out.append(0)

        for i in range(1, (n) // 2 + 1):
            out.append(i)
            out.append(-i)
        return out

