# 1358. Number of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
from collections import deque
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        queue_a = deque()
        queue_b = deque()
        queue_c = deque()
        for i in range(len(s)):
            if s[i] == "a":
                queue_a.appendleft(i)
            elif s[i] == "b":
                queue_b.appendleft(i)
            else:
                queue_c.appendleft(i)
        i = 0
        n = len(s)

        res = 0

        while (queue_a and queue_b and queue_c):
            if s[i] == "a":
                v = max(queue_b[-1], queue_c[-1])

                queue_a.pop()
            elif s[i] == "b":
                v = max(queue_a[-1], queue_c[-1])

                queue_b.pop()
            else:
                v = max(queue_b[-1], queue_a[-1])

                queue_c.pop()

            res += n - v
            i += 1
        return res


