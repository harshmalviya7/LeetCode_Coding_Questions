# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum = 0
        s = 0
        for i in gain:
            s += i
            maximum = max(s, maximum)

        return maximum