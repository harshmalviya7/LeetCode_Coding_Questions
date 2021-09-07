# 1941. Check if All Characters Have Equal Number of Occurrences
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        c = Counter(s)
        a = c[s[0]]
        for i in c:
            if c[i] != a:
                return False
        return True

