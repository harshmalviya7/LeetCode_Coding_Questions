# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0 for _ in range(len(t))]
        stack = []
        for i in range(len(t)):
            while (stack and t[stack[-1]] < t[i]):
                a = stack.pop()
                res[a] = i - a

            stack.append(i)
        return res

