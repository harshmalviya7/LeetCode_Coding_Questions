# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        out = 0
        e = []
        for j, i in enumerate(points):
            heapq.heappush(e, (-(i[0] * i[0] + i[1] * i[1]), i))
            if len(e) > k:
                heapq.heappop(e)
            # a=(i[0]**2+i[1]**2)
            # e.append([a,i])
        return [j for i, j in e]
        # return [x[1] for x in sorted(e)][:k]


