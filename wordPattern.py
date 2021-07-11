# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()

        if len(s) != len(pattern):
            return False
        d = {}
        for i in range(len(s)):
            if pattern[i] not in d:
                if s[i] in d.values():
                    return False
                else:
                    d[pattern[i]] = s[i]

            elif d[pattern[i]] != s[i]:
                return False

        return True
