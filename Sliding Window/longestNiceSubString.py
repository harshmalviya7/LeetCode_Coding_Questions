# 1763. Longest Nice Substring
# https://leetcode.com/problems/longest-nice-substring/
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        se = set()
        for i in s:
            se.add(i)

        for i in range(0, len(s)):
            if s.find(str(s[i]).lower()) != -1 and s.find(str(s[i]).upper()) != -1:
                continue
            prev = self.longestNiceSubstring(s[:i])
            nextt = self.longestNiceSubstring(s[i + 1:])

            return prev if len(prev) >= len(nextt) else nextt
        return s

