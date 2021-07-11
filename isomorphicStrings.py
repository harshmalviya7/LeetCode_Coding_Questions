# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):

            if s[i] not in d:
                if t[i] in d.values():
                    return False
                else:
                    d[s[i]] = t[i]

            elif d[s[i]] != t[i]:
                return False

        return True