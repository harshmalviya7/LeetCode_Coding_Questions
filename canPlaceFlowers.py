# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        a = len(flowerbed)
        c = 0
        for i in range(a):

            if flowerbed[i] == 0:
                prev = 0 if i == 0 or flowerbed[i - 1] == 0 else 1
                nextt = 0 if i == a - 1 or flowerbed[i + 1] == 0 else 1

                if nextt == 0 and prev == 0:
                    flowerbed[i] = 1
                    c += 1
        return c >= n
