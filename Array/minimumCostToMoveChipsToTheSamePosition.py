# 1217. Minimum Cost to Move Chips to The Same Position
# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        e=0
        o=0
        for i in position:
            if i%2==0:
                e+=1
            else:
                o+=1
        return min(e,o)