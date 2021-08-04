# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, ob: List[List[int]]) -> int:

        n = len(ob)
        m = len(ob[0])

        if ob[0][0] or ob[-1][-1]:
            return 0
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    if ob[i][j] == 1 or (i != 0 and ob[i - 1][j] == 0) or (j != 0 and ob[i][j - 1] == 0):
                        ob[i][j] = 0
                    else:
                        ob[i][j] = 1

                else:
                    if ob[i][j] == 1:
                        ob[i][j] = 0
                    else:
                        ob[i][j] = ob[i - 1][j] + ob[i][j - 1]

        return ob[-1][-1]
