# 1450. Number of Students Doing Homework at a Given Time
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        a=0
        for i,j in zip(startTime,endTime):
            if i<=queryTime and j>=queryTime:
                a+=1
        return a