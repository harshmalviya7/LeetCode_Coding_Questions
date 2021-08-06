# 1160. Find Words That Can Be Formed by Characters
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        d = defaultdict(int)
        for i in chars:
            d[i] += 1
        ans = 0
        for j in words:
            a = d.copy()
            c = 1
            for i in j:
                a[i] -= 1
                if a[i] < 0:
                    c = 0
                    break
            if c:
                ans += len(j)
        return ans