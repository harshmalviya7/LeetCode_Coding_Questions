# 728. Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for i in range(left, right + 1):
            a = i
            flag = 0
            while (a):
                c = a % 10
                if c == 0 or i % c != 0:
                    flag = 1
                    break
                a //= 10

            if not flag:
                l.append(i)
        return l
