# 657. Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin/
class Solution:
    def judgeCircle(self, moves: str) -> bool:

        a , b =0 ,0
        for i in moves:
            if i== "U":
                a += 1
            elif i == "D":
                a -= 1
            elif i == "L":
                b -= 1
            elif i == "R":
                b += 1
        return a == 0 and b == 0

