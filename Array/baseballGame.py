# 682. Baseball Game
# https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l = []
        for i in ops:
            if i == "+":
                l.append(l[-1] + l[-2])
            elif i == "C":
                l.pop()
            elif i == "D":
                l.append(l[-1] * 2)
            else:
                l.append(int(i))

        return sum(l)