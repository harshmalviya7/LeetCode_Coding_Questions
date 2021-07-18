# 927. Three Equal Parts
# https://leetcode.com/problems/three-equal-parts/
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        a = [-1, -1]
        summ = sum(arr)
        if summ % 3 != 0:
            return a
        if summ == 0:
            return [0, 2]
        total1 = summ // 3
        no = 0
        n = len(arr)
        f, s, t = -1, -1, -1

        for i in range(n):
            if arr[i] == 1:
                no += 1
                if no == 1:
                    f = i
                elif no == total1 + 1:
                    s = i
                elif no == 2 * total1 + 1:
                    t = i
                    break

        while (t < n):
            if arr[f] == arr[s] and arr[s] == arr[t]:
                f += 1
                s += 1
                t += 1
            else:
                return a
        return [f - 1, s]

