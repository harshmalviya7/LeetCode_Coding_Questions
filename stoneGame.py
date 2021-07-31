# 877. Stone Game
# https://leetcode.com/problems/stone-game/
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        l = 0
        r = len(piles) - 1
        alex = 0
        lee = 0
        d = 0
        while (l <= r):
            if d == 0:
                if piles[l] < piles[r]:
                    alex += piles[r]
                    r -= 1
                else:
                    alex += piles[l]
                    l += 1

            elif d == 1:
                if piles[l] < piles[r]:
                    lee += piles[l]
                    l += 1
                else:
                    lee += piles[r]
                    r -= 1
            d = (d + 1) % 2

        return True if alex > lee else False