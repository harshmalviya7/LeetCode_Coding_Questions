# 859. Buddy Strings
# https://leetcode.com/problems/buddy-strings/
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            seen = set()
            for i in s:
                if i in seen:
                    return True
                seen.add(i)
            return False

        c = []
        for i, j in zip(s, goal):
            if i != j:
                c.append((i, j))
            if len(c) >= 3:
                return False
        return len(c) == 2 and c[0] == c[1][::-1]
