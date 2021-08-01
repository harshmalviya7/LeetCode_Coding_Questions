# 1769. Minimum Number of Operations to Move All Balls to Each Box
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        l = [0] * n
        c = 1 if boxes[0] == "1" else 0
        for i in range(1, n):
            l[i] = l[i - 1] + c
            c += 1 if boxes[i] == "1" else 0
        r = [0] * n
        c = 1 if boxes[-1] == "1" else 0
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] + c
            c += 1 if boxes[i] == "1" else 0

        return [sum(i) for i in zip(l, r)]