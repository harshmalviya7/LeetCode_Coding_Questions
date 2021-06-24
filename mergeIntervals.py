# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval s =sorted(intervals)

        #         if len(intervals)==1:
        #             return intervals
        output_star t =intervals[0][0]
        output_en d =intervals[0][1]
        outpu t =[]

        for i in range(1 ,len(intervals)):

            if output_en d> =intervals[i][0]:
                output_en d =max(intervals[i][1] ,output_end)
            else:
                output.append([output_start ,output_end])
                output_star t =intervals[i][0]
                output_en d =intervals[i][1]

        output.append([output_start ,output_end])



        return output
