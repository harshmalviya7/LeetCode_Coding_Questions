# 1684. Count the Number of Consistent Strings
# https://leetcode.com/problems/count-the-number-of-consistent-strings/
from collections import Counter
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d = Counter(allowed)
        res = 0
        for word in words:
            c = 0
            for i in word:

                if i not in d:
                    c = 1
                    break

            if not c:
                res += 1

        return res



