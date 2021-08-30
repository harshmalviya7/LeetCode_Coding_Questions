# 598. Range Addition II
# https://leetcode.com/problems/range-addition-ii/
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n
        m1, n1 = m, n
        for i in ops:
            if m1 > i[0]:
                m1 = i[0]
            if n1 > i[1]:
                n1 = i[1]

        return m1 * n1