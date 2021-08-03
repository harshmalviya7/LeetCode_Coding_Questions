# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ou t =0 e=[]
        for j,i in enu merate(points):

            a=(i[0]** 2+ i[ 1] **2)**0.5
            e.appe nd([a,i])

        return [x[1] for x in sorted(e)][:k]


