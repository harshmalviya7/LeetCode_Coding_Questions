# 202. Happy Number
# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:

        a = set()
        while (True):
            if n in a or n == 1:
                break
            a.add(n)
            l = 0
            r = len(str(n)) - 1
            c = 0
            while (l < r):
                c += int(str(n)[l]) ** 2 + int(str(n)[r]) ** 2
                l += 1
                r -= 1
            if len(str(n)) % 2 != 0:
                c += int(str(n)[l]) ** 2
            n = c

        if n == 1:
            return True
        return False