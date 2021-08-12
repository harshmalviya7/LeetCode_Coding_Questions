# 1266. Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        c=0
        for i in range(len(points)-1):
            a,b=points[i][0],points[i][1]
            p,q=points[i+1][0],points[i+1][1]
            c+=max(abs(p-a),abs(q-b))
        return c