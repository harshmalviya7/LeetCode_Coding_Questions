# 434. Number of Segments in a String
# https://leetcode.com/problems/number-of-segments-in-a-string/
class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0

        return len(s.split())
