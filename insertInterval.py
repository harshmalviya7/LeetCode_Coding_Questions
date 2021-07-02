# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []

        while (i < len(intervals) and intervals[i][0] < newInterval[0]):
            res.append(intervals[i])
            i += 1

        if not res or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1][1] = max(newInterval[1], res[-1][1])

        while (i < len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            i += 1

        return res
